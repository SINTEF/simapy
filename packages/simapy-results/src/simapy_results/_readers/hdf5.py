"""HDF5 result files.

Dispatch is on the file's root ``format`` attribute, as SIMA does it:
``simos_r0`` goes to :mod:`simapy_results._readers.simos_r0`, everything else --
including a file with no ``format`` at all -- stays here. One reader covers
``ts_buffer.b5`` and ``Riflex_Results.h5`` alike.

Dataset rank decides the kind of signal:

===== ============================================ ==========================
rank  meaning                                      values
===== ============================================ ==========================
0     a scalar                                     one value
1     equally spaced -- ``start`` / ``delta``       y only; x is implied
1     no ``delta``                                  y only; x is the index
2     ``(2, N)``: an explicit x row and a y row     both
other flattened, shape kept in ``dimension``       y only; x is the index
===== ============================================ ==========================

Rank 1 is why this reader exists. A SIMO time series is stored as bare y with a
``delta`` attribute and no x anywhere in the file; reconstructing the axis from
``start``/``delta`` is what keeps a long run from paying for an x array per
signal.

Group names may be shortened model ids. RIFLEX shortens names for the solvers and
every result format echoes the short form: ``sima_elmfor.h5`` keys its groups by
``Moor1e20`` where the model says ``MooringLine1``. The mpf reader resolves these
through the same map, and so does this one, so the two sources describe one line
rather than two.

Reading is in two passes, as in the mpf reader, but for a different reason. h5py
hands out dataset objects that die when the file closes, and holding every
result file open for the lifetime of the tree would leak descriptors. So the
structure pass records each dataset's path, shape and attributes -- all metadata,
no values -- and the value pass reopens the file and slices. Reopening costs a
file open per read; the alternative costs an open handle per file, forever.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, ClassVar

import numpy as np

from .._build import (
    add_signal,
    get_or_create_child,
    graft,
    rename,
    set_attribute,
    set_type,
    update_attributes,
)
from .._node import Container, Equidistant, Signal
from .._registry import register
from .._sources import Source, SourceError
from .._units import guard_unscaled, map_unit

#: SIMA's ``SignalConstants.BODY``: the type of a body container, and its attribute naming the body.
BODY = "body"

#: The attribute naming a node's type, and the older name still accepted.
TYPE_ATTRIBUTES = ("type", "class")

#: HDF5 keys cannot hold '.', '/' or non-ASCII, so the exporter writes
#: 'EFF_ TENSION' as the key and keeps 'EFF. TENSION' in this attribute. Here a
#: name is a field rather than an attribute, so it is promoted explicitly.
NAME_ATTRIBUTE = "name"

#: Attributes naming a unit.
UNIT_ATTRIBUTES = {"unit", "xunit", "yunit"}

#: The y unit is spelled ``yunit`` in HDF5 and ``unit`` in the signals model.
#: AbstractSignal.getYUnit reads yunit and falls back to unit; this package uses
#: one canonical name so that find(unit=...) and frames work on either source.
Y_UNIT_ALIASES = ("yunit", "unit")

FORMAT_ATTRIBUTE = "format"


def _h5py():
    try:
        import h5py  # pylint: disable=import-outside-toplevel
    except ImportError as exc:
        raise SourceError(
            "h5py is required to read HDF5 results but is not installed"
        ) from exc
    return h5py


def _single(value: Any) -> Any:
    """The one element of a size-1 array, the value itself if not an array, else None."""
    if isinstance(value, np.ndarray):
        return value.flat[0] if value.size == 1 else None
    return value


def _text(value: Any, strip: bool = False) -> str | None:
    """An attribute or dataset value as a string, or None if it is not textual."""
    value = _single(value)
    if isinstance(value, bytes):
        value = value.decode("utf-8", "replace")
    if not isinstance(value, str):
        return None
    return value.strip() if strip else value


def _number(value: Any) -> float | None:
    """An attribute or dataset value as a float, or None if it is not one number."""
    value = _single(value)
    if isinstance(value, (int, float, np.integer, np.floating)) and not isinstance(
        value, bool
    ):
        return float(value)
    return None


class _Dataset:
    """Where a dataset lives, so the value pass can reopen it.

    Nothing is cached: a caller who needs an array twice should keep it. Caching
    here would give back the memory that laziness just saved.
    """

    __slots__ = ("path", "name", "shape")

    def __init__(self, path: Path, name: str, shape: tuple[int, ...]):
        self.path = path
        self.name = name
        self.shape = shape

    def read(self, item=Ellipsis) -> np.ndarray:
        h5py = _h5py()
        with h5py.File(self.path, "r") as handle:
            dataset = handle[self.name]
            if h5py.check_string_dtype(dataset.dtype) is not None:
                dataset = dataset.asstr()
            return np.asarray(dataset[item])


class _Rank1Values(Equidistant):
    """A bare y-vector on an implied axis."""

    def __init__(self, dataset: _Dataset, xstart: float, xdelta: float, y_factor: float):
        super().__init__(dataset.shape[0], xstart, xdelta)
        self._dataset = dataset
        self._y_factor = y_factor

    def y(self) -> np.ndarray:
        return self._dataset.read().astype(np.float64) / self._y_factor


class _Rank2Values:
    """An explicit ``(2, N)`` x/y pair."""

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, dataset: _Dataset, x_factor: float, y_factor: float):
        self._dataset = dataset
        self._x_factor = x_factor
        self._y_factor = y_factor

    @property
    def size(self) -> int:
        return self._dataset.shape[1]

    def x(self) -> np.ndarray:
        return self._dataset.read(0).astype(np.float64) / self._x_factor

    def y(self) -> np.ndarray:
        return self._dataset.read(1).astype(np.float64) / self._y_factor


class _ScalarValues:
    """A rank-0 dataset: one value."""

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    size = 1

    def __init__(self, dataset: _Dataset, y_factor: float):
        self._dataset = dataset
        self._y_factor = y_factor

    def x(self) -> np.ndarray:
        return np.zeros(1)

    def y(self) -> np.ndarray:
        return self._dataset.read().reshape(1).astype(np.float64) / self._y_factor


class _ArrayValues:
    """A rank-1 dataset with no delta, or a flattened higher-rank one."""

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, dataset: _Dataset, y_factor: float = 1.0, numeric: bool = True):
        self._dataset = dataset
        self._y_factor = y_factor
        self._numeric = numeric
        self._size = int(np.prod(dataset.shape)) if dataset.shape else 1

    @property
    def size(self) -> int:
        return self._size

    def x(self) -> np.ndarray:
        return np.arange(self._size, dtype=np.float64)

    def y(self) -> np.ndarray:
        raw = self._dataset.read().reshape(-1)
        if not self._numeric:
            return raw
        return raw.astype(np.float64) / self._y_factor


@register
class Hdf5Reader:  # pylint: disable=too-few-public-methods
    """The unformatted HDF5 layout."""

    types: ClassVar[frozenset[str]] = frozenset({"h5", "hdf5", "b5"})

    def read(self, source: Source, into: Container) -> None:
        """Read one HDF5 file into a fresh container. See ``Reader.read``.

        The root ``format`` attribute picks the layout, as
        SIMA does: ``simos_r0`` is SIMO's, anything else
        -- including no attribute at all -- is the unformatted one.
        """
        # Imported here because simos_r0 borrows this module's value classes.
        from . import simos_r0  # pylint: disable=import-outside-toplevel  # circular

        h5py = _h5py()
        target = Container() if _SIMO_RESULTS.match(source.file) else into
        with h5py.File(source.path, "r") as handle:
            if _text(handle.attrs.get(FORMAT_ATTRIBUTE)) == simos_r0.FORMAT:
                simos_r0.read(handle, target, source)
            else:
                self._add_group(handle, target, h5py, source)
        if target is not into:
            _add_simo_results(target, into)

    def _add_group(self, group, container: Container, h5py, source: Source) -> None:
        for name, member in group.items():
            if isinstance(member, h5py.Group):
                # Looked up by the raw key, then renamed, so two
                # containers sharing a resolved name stay separate here and are
                # merged later, by name.
                child = get_or_create_child(container, name)
                _apply_attributes(child, member.attrs)
                rename(child, source.context.resolve_id(child.name))
                self._add_group(member, child, h5py, source)
            else:
                add_signal(container, _to_signal(name, member, source.path))


#: SIMO's own result files, which SIMA reads with ``SIMOHDF5ResultsImporter``
#: (types ``simo_stamod_hdf5`` and ``simo_dynmod_hdf5``) rather than as plain HDF5.
_SIMO_RESULTS = re.compile(r"\Asimo-(static|dynamic)-results(-[^.]+)?\.h5\Z", re.IGNORECASE)


def _add_simo_results(root: Container, into: Container) -> None:
    """``SIMOHDF5ResultsImporter``: drop the root ``results`` level, and make each body a body container."""
    results = next((child for child in root.containers if child.name == "results"), None)
    if results is None:
        return
    for child in results.containers:
        if child.name in ("Bodies", "bodies"):
            for body in child.containers:
                container = get_or_create_child(into, body.name)
                set_attribute(container, BODY, body.name)
                set_type(container, BODY)
                for grandchild in body.containers:
                    graft(container, grandchild)
                for signal in body.signals:
                    add_signal(container, signal)
        else:
            graft(into, child)


def _apply_attributes(node, attrs) -> None:
    """Copy the textual attributes across. Non-textual ones are not metadata.

    A ``name`` attribute becomes the node's name rather than an attribute of it:
    it is the true name the HDF5 key could not spell.
    """
    for key in attrs:
        text = _text(attrs[key])
        if text is None:
            continue
        if key == NAME_ATTRIBUTE:
            rename(node, text)
        else:
            set_attribute(node, key, text)


def _signal_attributes(dataset) -> tuple[dict[str, str], float, float, dict[str, str]]:
    """Textual attributes, the x and y unit factors, and the raw unit labels.

    The raw labels come back alongside the converted ones because
    :func:`~simapy_results._units.guard_unscaled` needs the label as the file
    wrote it, not the base unit it resolved to.

    Anything that is not text is ignored, which is how ``delta`` and ``start``
    stay out of the attribute map and describe the axis instead. Unit attributes
    are converted to base units and their factor kept, as SIMA does.
    """
    attributes: dict[str, str] = {}
    x_factor = y_factor = 1.0
    raw: dict[str, str] = {}

    for key in dataset.attrs:
        text = _text(dataset.attrs[key])
        if text is None:
            continue
        if key in UNIT_ATTRIBUTES:
            base, factor = map_unit(text)
            if key == "xunit":
                x_factor = factor
                attributes["xunit"] = base
                raw["xunit"] = text
            else:
                # yunit and unit both land on the canonical name.
                y_factor = factor
                attributes["unit"] = base
                raw["unit"] = text
        elif key in TYPE_ATTRIBUTES:
            attributes["type"] = text
        else:
            attributes[key] = text
    return attributes, x_factor, y_factor, raw


def _to_signal(name: str, dataset, path: Path) -> Signal:
    """One dataset as a signal, with rank deciding the kind."""
    attributes, x_factor, y_factor, raw_units = _signal_attributes(dataset)

    rank = len(dataset.shape)
    numeric = dataset.dtype.kind in "fiu"
    handle = _Dataset(path, dataset.name, tuple(dataset.shape))
    delta = _number(dataset.attrs.get("delta"))

    if not numeric:
        values = _ArrayValues(handle, numeric=False)
    elif rank == 0:
        values = _ScalarValues(handle, y_factor)
    elif rank == 2 and dataset.shape[0] == 2:
        values = _Rank2Values(handle, x_factor, y_factor)
    elif rank == 1 and delta is not None:
        values = _Rank1Values(
            handle,
            xstart=(_number(dataset.attrs.get("start")) or 0.0) / x_factor,
            xdelta=delta / x_factor,
            y_factor=y_factor,
        )
    else:
        values = _ArrayValues(handle, y_factor)
        if rank > 1:
            # The shape is kept once the data is flat.
            attributes["dimension"] = ",".join(str(d) for d in dataset.shape)

    signal_name = attributes.pop(NAME_ATTRIBUTE, name)
    guarded, marks = guard_unscaled(
        values, f"{path.name}/{signal_name}",
        raw_units.get("unit"), raw_units.get("xunit"),
    )
    signal = Signal(signal_name, guarded)
    update_attributes(signal, attributes)
    update_attributes(signal, marks)
    return signal

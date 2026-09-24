"""The ``simos_r0`` HDF5 layout SIMO writes.

Reached from :mod:`simapy.results._readers.hdf5` when a file's root ``format``
attribute says ``simos_r0``. SIMO serialises its result types generically, so
the layout follows from the type definitions rather than being a designed file
format.

Two things make it unlike the unformatted layout:

* **Metadata is in child datasets, not attributes.** A signal is a *group* whose
  ``type`` attribute names a marmo container, holding ``value``, ``unit``,
  ``name`` and the axis members as separate rank-1 datasets.
* **Containers are named by a ``name`` dataset.** Array members are keyed ``0``,
  ``1``, ``2`` in the file, so without promoting that dataset every body reads as
  ``0``.

**Values are rescaled**, dividing by the unit's factor and reporting the base
unit, so a ``kN`` signal is served as N. Reading the datasets untouched would
disagree with SIMA by a factor of 1000 on most of the forces in a SIMO result.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from .._build import add_signal, get_or_create_child, rename, set_attribute
from .._node import Container, ErrorSignal, Signal
from .._sources import Source, SourceError
from .._units import guard_unscaled, map_unit
from .hdf5 import (
    _ArrayValues,
    _Dataset,
    _number,
    _Rank1Values,
    _ScalarValues,
    _text,
    _to_signal,
)

if TYPE_CHECKING:  # pragma: no cover
    from pathlib import Path

#: Value of the root ``format`` attribute this module claims.
FORMAT = "simos_r0"

#: Every container type is under this prefix. ``isMarmoType``.
_MARMO_PREFIX = "marmo"

#: Names the enclosing container rather than being a result of its own.
#: ``isSimosInternalDataset``.
_INTERNAL_DATASETS = frozenset({"name"})

#: Carried across as metadata where the container types provide them.
_DESCRIPTIVE = ("label", "legend", "description", "xdescription", "xlabel", "xname")


def read(handle, into: Container, source: Source) -> None:
    """Read an open ``simos_r0`` file into a container. ``importResults``.

    Args:
        handle: An open ``h5py.File``.
        into: The container to fill.
        source: The result file being read, for paths and id resolution.
    """
    for name in handle:
        member = handle[name]
        if _is_group(member):
            _add_group(member, into, source)


def _add_group(group, parent: Container, source: Source) -> None:
    """One group: a signal if it is a marmo container, else a container."""
    if _marmo_type(group) is not None:
        add_signal(parent, _marmo_signal(group, source.path))
        return
    child = get_or_create_child(parent, group.name.rsplit("/", 1)[-1])
    rename(child, source.context.resolve_id(_folder_name(group)))
    for name in group:
        member = group[name]
        if _is_group(member):
            _add_group(member, child, source)
    _add_datasets(group, child, source.path)


def _add_datasets(group, container: Container, path: Path) -> None:
    """Loose datasets beside the child groups. ``importAtomicData``.

    These are unformatted-style: any units are attributes, as they are in the
    files RIFLEX writes, so this is the same conversion the other reader does.
    """
    for name in group:
        member = group[name]
        if not _is_group(member) and name not in _INTERNAL_DATASETS:
            add_signal(container, _to_signal(name, member, path))


def _marmo_signal(group, path: Path) -> Signal:
    """A marmo container group as one signal. ``importMarmoGroup``.

    An unsupported container type leaves an :class:`ErrorSignal` rather than
    failing the file. SIMA raises here, but a reader in this package is
    best-effort by contract: one unreadable signal must not cost the caller the
    other three thousand.
    """
    type_name = _marmo_type(group)
    builder = _BUILDERS.get(type_name)
    if builder is None:
        error = SourceError(
            f"{group.name}: unsupported marmo container {type_name!r}. "
            "the simos_r0 layout implements EquallySpacedSignal, "
            "NonEquallySpacedSignal, DimensionalScalar and SimpleString."
        )
        return ErrorSignal(group.name.rsplit("/", 1)[-1], error)
    try:
        return builder(group, path)
    except (KeyError, ValueError, TypeError, IndexError, AttributeError) as failure:
        return ErrorSignal(
            group.name.rsplit("/", 1)[-1],
            SourceError(f"{group.name}: {failure}"),
        )


def _equally_spaced(group, path: Path) -> Signal:
    """``importEquallySpacedSignal``: a y-vector on an implied axis."""
    name = _required_text(group, "name")
    raw_unit, raw_xunit = _required_text(group, "unit"), _required_text(group, "xunit")
    y_unit, y_factor = map_unit(raw_unit)
    x_unit, x_factor = map_unit(raw_xunit)
    # The axis is declared in the file's unit, so it is scaled with it.
    xstart = _member_number(group, "xstart") / x_factor
    xdelta = _member_number(group, "xdelta") / x_factor

    values = group["value"]
    guarded, marks = guard_unscaled(
        _Rank1Values(_Dataset(path, values.name, values.shape), xstart, xdelta, y_factor),
        group.name, raw_unit, raw_xunit,
    )
    signal = Signal(name, guarded, type=_marmo_type(group),
                    unit=y_unit, xunit=x_unit, **marks)
    return _with_descriptions(signal, group)


def _non_equally_spaced(group, path: Path) -> Signal:
    """``importNonEquallySpacedSignal``: parallel x and y vectors."""
    name = _required_text(group, "name")
    raw_unit, raw_xunit = _required_text(group, "unit"), _required_text(group, "xunit")
    y_unit, y_factor = map_unit(raw_unit)
    x_unit, x_factor = map_unit(raw_xunit)

    values, abscissa = group["value"], group["xvalue"]
    guarded, marks = guard_unscaled(
        _PairedValues(
            _Dataset(path, abscissa.name, abscissa.shape),
            _Dataset(path, values.name, values.shape),
            x_factor,
            y_factor,
        ),
        group.name, raw_unit, raw_xunit,
    )
    signal = Signal(name, guarded, type=_marmo_type(group),
                    unit=y_unit, xunit=x_unit, **marks)
    return _with_descriptions(signal, group)


def _dimensional_scalar(group, path: Path) -> Signal:
    """``importDimensionalScalar``: one value with a unit."""
    name = _required_text(group, "name")
    # The unit defaults to "?" rather than being required.
    raw_unit = _member_text(group, "unit") or "?"
    unit, factor = map_unit(raw_unit)

    values = group["value"]
    guarded, marks = guard_unscaled(
        _ScalarValues(_Dataset(path, values.name, values.shape), factor),
        group.name, raw_unit,
    )
    signal = Signal(name, guarded, type=_marmo_type(group), unit=unit, **marks)
    return _with_descriptions(signal, group)


def _simple_string(group, path: Path) -> Signal:
    """``importSimpleString``: a named string."""
    name = _required_text(group, "name")
    values = group["value"]
    signal = Signal(
        name,
        _ArrayValues(_Dataset(path, values.name, values.shape), numeric=False),
        type=_marmo_type(group),
    )
    return _with_descriptions(signal, group)


_BUILDERS = {
    "marmo:containers:EquallySpacedSignal": _equally_spaced,
    "marmo:containers:NonEquallySpacedSignal": _non_equally_spaced,
    "marmo:containers:DimensionalScalar": _dimensional_scalar,
    "marmo:containers:SimpleString": _simple_string,
}


class _PairedValues:
    """x and y as two rank-1 datasets, which is how the marmo containers store them.

    ``_Rank2Values`` in the unformatted reader is the same idea over a single
    ``(2, N)`` dataset; here the two axes are separate members of the group.
    """

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, abscissa, ordinate, x_factor: float, y_factor: float):
        self._abscissa = abscissa
        self._ordinate = ordinate
        self._x_factor = x_factor
        self._y_factor = y_factor
        self._size = int(np.prod(ordinate.shape))

    @property
    def size(self) -> int:
        return self._size

    def x(self) -> np.ndarray:
        # An x row of another length cannot pair with y, so it falls back to the index.
        if int(np.prod(self._abscissa.shape)) != self._size:
            return np.arange(self._size, dtype=np.float64)
        return self._abscissa.read().reshape(-1).astype(np.float64) / self._x_factor

    def y(self) -> np.ndarray:
        return self._ordinate.read().reshape(-1).astype(np.float64) / self._y_factor


def _with_descriptions(signal: Signal, group) -> Signal:
    """Carry across the labels SIMA shows, where the container has them."""
    for member in _DESCRIPTIVE:
        text = _member_text(group, member)
        if text:
            set_attribute(signal, member, text)
    return signal


def _is_group(member) -> bool:
    return hasattr(member, "keys")


def _marmo_type(group) -> str | None:
    """The container type, or None when the group is not one. ``isMarmoType``."""
    type_name = _text(group.attrs.get("type"), strip=True)
    if type_name and type_name.startswith(_MARMO_PREFIX):
        return type_name
    return None


def _folder_name(group) -> str:
    """The ``name`` dataset, else the HDF5 key. ``findFolderName``.

    Array members are keyed ``0``, ``1``, ``2``, so this is what gives a body its
    name instead of its index.
    """
    return _member_text(group, "name") or group.name.rsplit("/", 1)[-1]


def _member_text(group, member: str) -> str | None:
    """A string dataset's single value, or None if it is absent or not a string."""
    if member not in group:
        return None
    return _text(group[member][()], strip=True)


def _required_text(group, member: str) -> str:
    """``getRequiredString``: absent or empty is a failure, not a default."""
    text = _member_text(group, member)
    if not text:
        raise ValueError(f"{member!r} is required, but is empty or does not exist")
    return text


def _member_number(group, member: str) -> float:
    """A numeric dataset's single value, 0.0 when absent."""
    if member not in group:
        return 0.0
    number = _number(group[member][()])
    if number is None:
        raise ValueError(f"{member!r} is not a single number")
    return number

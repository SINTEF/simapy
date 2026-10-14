"""The SIMA signals model as JSON, as a workflow's file output node writes it.

The node writes the same containers and signals as HDF5 or as JSON, so this
reader gives the tree the HDF5 reader would: same names, values converted to
base units the same way.

Eager, unlike the other readers: a JSON document is parsed whole before it can
name a signal, so the values are already in hand and are kept as arrays.

Folder scans skip ``.json``. A workflow writes its input and its output as the
same model in the same folder, so only a caller naming the file knows which is
which.
"""

from __future__ import annotations

import json
from typing import Any, ClassVar

import numpy as np

from .._build import add_signal, get_or_create_child, update_attributes
from .._node import Container, Equidistant, Signal
from .._registry import register
from .._sources import Source, SourceError
from .._units import guard_unscaled, map_unit

#: ``sima/signals/Container``, the only content type that nests.
CONTAINER = "Container"

#: Types whose ``value`` is one number rather than a series.
SCALARS = frozenset({"DimensionalScalar", "IntegerScalar", "SimpleBoolean"})

#: Types whose ``value`` is a series with no x-axis of its own.
ARRAYS = frozenset({"IntegerArray", "BooleanArray", "DimensionalMatrix"})

#: Types whose values are text, so ``y`` stays a string array.
TEXT = frozenset({"SimpleString", "StringArray"})

#: Defined by the signal's own fields, so an ``attributes`` entry cannot override them.
RESERVED_ATTRIBUTES = frozenset({"name", "unit", "xunit", "yunit"})


def _frozen(array: np.ndarray) -> np.ndarray:
    array.flags.writeable = False
    return array


class _Values:
    """Values already in memory, on an explicit x-axis."""

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, x: np.ndarray, y: np.ndarray):
        self._x = _frozen(x)
        self._y = _frozen(y)

    @property
    def size(self) -> int:
        return int(self._y.size)

    def x(self) -> np.ndarray:
        return self._x

    def y(self) -> np.ndarray:
        return self._y


class _EquidistantValues(Equidistant):
    """Values on an implied x-axis, as ``EquallySpacedSignal`` stores them."""

    def __init__(self, y: np.ndarray, xstart: float, xdelta: float):
        super().__init__(int(y.size), xstart, xdelta)
        self._y = _frozen(y)

    def y(self) -> np.ndarray:
        return self._y


def _kind(item: dict) -> str:
    """The type name without its package, or "" for an item that has no type."""
    return str(item.get("type", "")).rsplit("/", maxsplit=1)[-1]


def _array(value: Any, dtype: Any = np.float64) -> np.ndarray:
    return np.asarray(value if value is not None else [], dtype=dtype).reshape(-1)


def _label(value: Any) -> str | None:
    """A unit label, or None for anything that is not a non-empty string."""
    return value if isinstance(value, str) and value else None


def _values(item: dict, kind: str, x_factor: float, y_factor: float):
    """The value provider for one signal in base units, or None if nothing here reads it."""
    if kind == "EquallySpacedSignal":
        xdelta = item.get("xdelta")
        return _EquidistantValues(
            _array(item.get("value")) / y_factor,
            float(item.get("xstart") or 0.0) / x_factor,
            (1.0 if xdelta is None else float(xdelta)) / x_factor,
        )
    if kind == "NonEquallySpacedSignal":
        y = _array(item.get("value")) / y_factor
        x = _array(item.get("xvalue"))
        # A missing x row would otherwise pair a full y against nothing.
        x = x / x_factor if x.size == y.size else np.arange(y.size, dtype=np.float64)
        return _Values(x, y)
    if kind in SCALARS:
        return _Values(np.zeros(1), _array([item.get("value", float("nan"))]) / y_factor)
    if kind in ARRAYS:
        y = _array(item.get("value")) / y_factor
        return _Values(np.arange(y.size, dtype=np.float64), y)
    if kind in TEXT:
        value = item.get("value")
        y = _array([value] if isinstance(value, str) else value, dtype=object)
        return _Values(np.arange(y.size, dtype=np.float64), y)
    return None


def _attributes(item: dict) -> dict[str, str]:
    """An item's own ``attributes`` list, as the tree's flat mapping."""
    found = {}
    for attribute in item.get("attributes", []) or []:
        name = attribute.get("name")
        if name and str(name) not in RESERVED_ATTRIBUTES:
            found[str(name)] = str(attribute.get("value", ""))
    return found


def _to_signal(item: dict, kind: str, file: str) -> Signal | None:
    raw_unit, raw_xunit = _label(item.get("unit")), _label(item.get("xunit"))
    unit, y_factor = map_unit(raw_unit)
    xunit, x_factor = map_unit(raw_xunit)
    values = _values(item, kind, x_factor, y_factor)
    if values is None:
        return None

    name = str(item.get("name", ""))
    attributes = _attributes(item)
    if raw_unit is not None:
        attributes["unit"] = unit
    if raw_xunit is not None:
        attributes["xunit"] = xunit
    guarded, marks = guard_unscaled(values, f"{file}/{name}", raw_unit, raw_xunit)
    signal = Signal(name, guarded)
    update_attributes(signal, attributes)
    update_attributes(signal, marks)
    return signal


def _add(items, container: Container, file: str) -> None:
    for item in items:
        if not isinstance(item, dict):
            continue
        kind = _kind(item)
        if kind == CONTAINER:
            child = get_or_create_child(container, str(item.get("name", "")))
            update_attributes(child, _attributes(item))
            _add(item.get("signals") or [], child, file)
            _add(item.get("containers") or [], child, file)
        else:
            signal = _to_signal(item, kind, file)
            if signal is not None:
                add_signal(container, signal)


@register
class SignalsJsonReader:  # pylint: disable=too-few-public-methods
    """The signals model SIMA writes as JSON."""

    types: ClassVar[frozenset[str]] = frozenset({"json"})

    def read(self, source: Source, into: Container) -> None:
        """Read one signals document into a fresh container. See ``Reader.read``.

        A document holding no signals -- ``commands.json``, an exported task --
        reads as nothing rather than as a failure. It is a valid SIMA model;
        it just has no results in it.
        """
        try:
            document = json.loads(source.path.read_text(encoding="utf-8"))
        except OSError as error:
            raise SourceError(f"cannot read {source.file}: {error}") from error
        except ValueError as error:
            raise SourceError(f"{source.file} is not valid JSON: {error}") from error

        if not isinstance(document, dict):
            raise SourceError(f"{source.file} is not a SIMA model document")
        _add(document.get("contents") or [], into, source.file)

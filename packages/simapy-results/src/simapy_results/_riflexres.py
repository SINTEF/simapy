"""``riflexres.inp``: what SIMA wrote beside a RIFLEX run about the model behind it.

A port of ``RIFLEXResultMapperImporter``. The MPF and HDF5 readers need only the
ids; RIFLEX storage files need the rest too -- the units RIFLEX wrote in, which
elements have angles stored, and the support vessels' names.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from ._units import SIMA_UNITS

#: Written by RIFLEX's ``RIFLEXResultMapperExporter`` beside every run.
RIFLEX_MAPPER_FILENAME = "riflexres.inp"

#: The base units SIMA's exporter assumes when the file predates its units section.
_OLD_EXPORT_UNITS: dict[str, str] = {"F": "kN", "M": "Mg", "W": "kW", "P": "kPa"}

#: (line id, segment, element)
ElementRef = tuple[str, int, int]


@dataclass(frozen=True)
class ElementAngle:
    """An element's angle with a global axis, projected in a global plane."""

    element: ElementRef
    plane: str
    axis: str


@dataclass(frozen=True)
class RiflexMapper:
    """What the storage import needs from ``riflexres.inp``; ``RIFLEXResultMapper``."""

    #: Short id to model name.
    ids: dict[str, str] = field(default_factory=dict)
    #: An element to the elements its relative angle is stored against.
    relative_angles: dict[ElementRef, tuple[ElementRef, ...]] = field(default_factory=dict)
    element_angles: tuple[ElementAngle, ...] = ()
    read_matrices: bool = False
    #: Base unit symbol to the label RIFLEX wrote values in: ``{"F": "kN"}``.
    units: dict[str, str] = field(default_factory=lambda: dict(_OLD_EXPORT_UNITS))
    support_vessels: tuple[str, ...] = ()

    def unit_factor(self, unit: str | None) -> float:
        """What to divide a stored value by to reach ``unit``. ``UnitEngine.getFactor``.

        ``unit`` is a base unit label such as ``N*m``; its atoms are looked up in
        the units RIFLEX wrote in, so ``N*m`` under ``F=kN`` is ``0.001``.
        """
        return _factor(unit, self.units)


#: Without the file, SIMA falls back to a default task's export units.
DEFAULT = RiflexMapper()


class MapperError(Exception):
    """``riflexres.inp`` is there but does not parse."""


def read_ids(folder: Path) -> dict[str, str]:
    """The ids alone, which an unreadable later section must not cost.

    Without them names stay hashed -- cosmetic, never a failure -- so a file
    that does not parse adds no names rather than half a map.
    """
    try:
        mapper = read_mapper(folder, ids_only=True)
    except MapperError:
        return {}
    return dict(mapper.ids) if mapper else {}


def read_mapper(folder: Path, ids_only: bool = False) -> RiflexMapper | None:
    """The folder's ``riflexres.inp``, or None if there is none or it predates 2.0.

    :raises MapperError: if the file does not parse. SIMA refuses the import
        then, and so must a reader: falling back to default units would scale
        the values wrongly without a word.
    """
    path = folder / RIFLEX_MAPPER_FILENAME
    try:
        stat = path.stat()
    except OSError:
        return None
    return _read_cached(path, stat.st_mtime_ns, stat.st_size, ids_only)


@lru_cache(maxsize=32)
def _read_cached(path: Path, _mtime: int, _size: int, ids_only: bool) -> RiflexMapper | None:
    try:
        text = path.read_text(encoding="utf-8")
        return _parse(iter(line for line in text.splitlines() if not line.startswith("'")), ids_only)
    except (OSError, UnicodeDecodeError, StopIteration, ValueError, IndexError) as exc:
        raise MapperError(f"{path.name} does not parse: {exc!r}") from exc


def _parse(rows, ids_only: bool) -> RiflexMapper | None:  # pylint: disable=too-many-branches  # a section each, in file order
    version = tuple(int(part) for part in next(rows).strip().split("."))
    if version < (2, 0, 0):
        return None
    ids: dict[str, str] = {}
    for _ in range(_int(rows)):
        key, value = _key_value(next(rows))
        ids[key] = value
        if version >= (2, 1, 0):
            for _ in range(_int(rows)):  # segments
                _skip(rows, _int(rows))  # their properties
    if ids_only:
        # Walked, not parsed: a section the ids do not need must not cost them.
        for _ in range(_int(rows)):  # relative angles
            _skip(rows, 3)
            _skip(rows, 3 * _int(rows))
        _skip(rows, 5 * _int(rows))  # element angles
        relative_angles: dict[ElementRef, tuple[ElementRef, ...]] = {}
        element_angles: tuple[ElementAngle, ...] = ()
    else:
        relative_angles = {}
        for _ in range(_int(rows)):
            element = _element(rows)
            relative_angles[element] = tuple(_element(rows) for _ in range(_int(rows)))
        element_angles = tuple(
            ElementAngle(_element(rows), next(rows).strip(), next(rows).strip())
            for _ in range(_int(rows))
        )
    if version >= (2, 6, 0):
        _skip(rows, 4 * _int(rows))  # transformations
    _skip(rows, 2 * _int(rows))  # stress storage
    if version >= (2, 1, 0):
        _skip(rows, 2 * _int(rows))  # load steps
    if version >= (2, 2, 0):
        for _ in range(_int(rows)):
            key, value = _key_value(next(rows))
            ids[key] = value
    if ids_only:
        return RiflexMapper(ids=ids)
    parameters: dict[str, str] = {}
    if version >= (2, 3, 0):
        for _ in range(_int(rows)):
            key, value = _key_value(next(rows))
            parameters[key] = value
    units = dict(_OLD_EXPORT_UNITS)
    if version >= (2, 4, 0):
        units = {}
        for _ in range(_int(rows)):
            symbol, label = _key_value(next(rows))
            units[_symbol_of(symbol.strip())] = label.strip()
    vessels: tuple[str, ...] = ()
    if version >= (2, 5, 0):
        vessels = tuple(next(rows) for _ in range(_int(rows)))
    return RiflexMapper(
        ids=ids,
        relative_angles=relative_angles,
        element_angles=element_angles,
        read_matrices=parameters.get("readMatrix", "false").strip().lower() == "true",
        units=units,
        support_vessels=vessels,
    )


def _int(rows) -> int:
    return int(next(rows))


def _element(rows) -> ElementRef:
    return next(rows).strip(), _int(rows), _int(rows)


def _key_value(row: str) -> tuple[str, str]:
    parts = row.split("=")
    return parts[0], parts[1]


def _skip(rows, count: int) -> None:
    for _ in range(count):
        next(rows)


# --------------------------------------------------------------------------
# UnitEngine.getFactor
# --------------------------------------------------------------------------

#: Base unit symbol or label to its symbol, as ``BaseUnitEngine.getUnit`` finds one.
_SYMBOLS: dict[str, str] = {
    **{base: symbol for symbol, (base, _) in SIMA_UNITS.items()},
    **{symbol: symbol for symbol in SIMA_UNITS},
}


def _symbol_of(symbol_or_label: str) -> str:
    symbol = _SYMBOLS.get(symbol_or_label)
    if symbol is None:
        raise ValueError(f"Unable to identify base unit with symbol {symbol_or_label}")
    return symbol


def _factor(unit: str | None, current: dict[str, str]) -> float:  # pylint: disable=too-many-return-statements
    """A port of ``UnitEngine.getFactor``, grammar and failures included."""
    if unit is None:
        return 1.0
    if "(" in unit:
        raise ValueError("Paranthesis are not allowed")
    if "/" in unit:
        if unit.count("/") > 1:
            raise ValueError("There can only be one division in units")
        dividend, divisor = unit.split("/", 1)
        return _factor(dividend, current) / _factor(divisor, current)
    if "*" in unit:
        first, rest = unit.split("*", 1)
        return _factor(first, current) * _factor(rest, current)
    if "^" in unit:
        base, exponent = unit.split("^", 1)
        return _factor(base, current) ** float(exponent)
    symbol = _symbol_of(unit.strip())
    label = current.get(symbol)
    if label is None:
        return 1.0
    base, alternatives = SIMA_UNITS[symbol]
    if label == base:
        return 1.0
    if label not in alternatives:
        raise ValueError(f"Undefined unit {label} for base unit {symbol}")
    return alternatives[label]

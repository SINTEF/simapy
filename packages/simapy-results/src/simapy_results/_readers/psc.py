"""SIMO's static results as text: ``psc.lis``, named by the ``simores.inp`` beside it.

A port of SIMA's ``PSCResultImporter``, ``PSCMetaDataImporter`` and
``StaticConditionResultFactory``, with ``SIMOResultMapperImporter`` for
``simores.inp``.

``psc.lis`` numbers what it holds -- body 1, its third coupling -- and SIMA names
each from the model it ran. A folder has no model, but SIMA writes the names into
``simores.inp`` beside every static run, so that file is required here; where
SIMA would fall back to the model, the source fails.

Values are in the model's units, the ones ``simores.inp`` lists, and are scaled
into base units as SIMA scales each result attribute by its unit annotation.

Parsed whole at open: the file is small and the tree is all constants.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

from .._build import add_signal, get_or_create_child, graft, set_attribute, set_type
from .._node import Container, constant
from .._registry import register
from .._sources import Source, SourceError
from .._units import SIMA_UNITS, map_unit, parse
from .hdf5 import BODY

#: SIMA writes this beside every static run: ``SIMOResultUtil.SIMO_RES_FILE``.
MAPPER_FILENAME = "simores.inp"

#: ``SignalConstants.NONDIMENSIONAL``, every signal's x unit.
NONDIMENSIONAL = "-"

FORCE = "N"
MOMENT = "N*m"
LENGTH = "m"
ANGLE = "deg"

_VACANT = "Vacant"

#: One per body-force row, in the file's order; see staarr.dat in SIMO.
_BODY_FORCES = (
    "Gravity",
    "Time dependent mass",
    "Retardation function",
    "Hydrostatics",
    "Linear damping",
    "Quadratic damping",
    "First order wave",
    _VACANT,  # full quadratic wave, unused in SIMO
    "Wind forces",
    "Linear current",
    "Quadratic current",
    "Distributed forces,slamming",
    "Distributed forces,volume",
    "Distributed forces,wave/current",
    "Second order wave drift, wind",
    "Wave drift damping",
    _VACANT,
    "Coupling forces",
    "Specified forces",
    "External forces",
    "Positioning elements",
    "Thruster",
    "Small body hydrodynamics",
    _VACANT,  # general line system, not in SIMA
    "Rigid body kinetics",
    _VACANT,
    "Slender system connection",
    "Second order wave drift, swell",
    "Total",
)

#: ``simores.inp`` lists its units from this version on.
_UNITS_SINCE = (3, 2, 0)

#: The units older ``simores.inp`` files were written in, by base unit symbol.
_DEFAULT_UNITS = {"F": "kN", "M": "Mg", "W": "kW", "P": "kPa"}

_VERSION = re.compile(r"\A(\d+)\.(\d+)\.(\d+)([.+-].*)?\Z")


class _Lines:
    """A file's lines, skipping those that start with ``'`` as both Java readers do."""

    def __init__(self, path: Path, encoding: str):
        try:
            with path.open(encoding=encoding, errors="replace", newline=None) as handle:
                self._lines = [line.rstrip("\n") for line in handle]
        except OSError as exc:
            raise SourceError(f"cannot read {path.name}: {exc}") from exc
        self._file = path.name
        self._number = 0

    def next(self) -> str:
        """The next uncommented line, untrimmed."""
        while self._number < len(self._lines):
            line = self._lines[self._number]
            self._number += 1
            if not line.startswith("'"):
                return line
        raise self.error("the file ends early")

    def error(self, message: str) -> SourceError:
        """A SourceError naming the file and the line last read."""
        return SourceError(f"{self._file} line {self._number}: {message}")

    def integer(self) -> int:
        """The next line as an integer."""
        text = self.next()
        try:
            return int(text)
        except ValueError:
            raise self.error(f"expected an integer, found {text.strip()!r}") from None

    def number(self) -> float:
        """The next line as a float."""
        text = self.next()
        try:
            return float(text)
        except ValueError:
            raise self.error(f"expected a number, found {text.strip()!r}") from None

    def numbers(self, size: int, what: str) -> list[float]:
        """The next line as exactly ``size`` whitespace-separated floats."""
        tokens = self.next().split()
        if len(tokens) != size:
            raise self.error(f"{what} should hold {size} values, found {len(tokens)}")
        try:
            return [float(token) for token in tokens]
        except ValueError:
            raise self.error(f"{what} holds a value that is not a number") from None


# -- simores.inp: SIMOResultMapperImporter -----------------------------------


@dataclass
class _Body:  # pylint: disable=too-many-instance-attributes
    """``BodyResultMapper``: what ``simores.inp`` says about one body."""

    name: str
    initial: list[float]
    specified_forces: list[str] = field(default_factory=list)
    specified_moments: list[str] = field(default_factory=list)
    external_forces: list[str] = field(default_factory=list)
    positioning_elements: list[str] = field(default_factory=list)
    thrusters: list[str] = field(default_factory=list)
    couplings: list[str] = field(default_factory=list)


@dataclass
class _Mapper:
    """``SIMOResultMapper``: the bodies in SIMO's order, and the model's units."""

    bodies: list[_Body]
    #: Base unit label to the model's label for it: ``{"N": "kN"}``.
    units: dict[str, str]

    def scale(self, unit: str) -> float:
        """``1.0 / UnitEngine.getFactor(unit)``: what a value in the model's units is multiplied by."""
        factor = 1.0
        for atom, exponent in parse(unit).items():
            factor *= map_unit(self.units.get(atom, atom))[1] ** exponent
        return 1.0 / factor


def _read_mapper(path: Path) -> _Mapper:
    lines = _Lines(path, "utf-8")
    text = lines.next().strip()
    match = _VERSION.match(text)
    if match is None:
        raise lines.error(f"expected a version, found {text!r}")
    version = tuple(int(part) for part in match.groups()[:3])
    if version < (2, 0, 0):
        raise lines.error(f"unsupported version {text}; rerun the condition")
    bodies = [_read_body_names(lines, version[0]) for _ in range(lines.integer())]
    if version >= _UNITS_SINCE:
        units = _read_units(lines)
    else:
        units = {SIMA_UNITS[symbol][0]: label for symbol, label in _DEFAULT_UNITS.items()}
    return _Mapper(bodies, units)


def _read_body_names(lines: _Lines, major: int) -> _Body:
    # Both names: the model's, then the one exported to SIMO. Older files have one.
    name = lines.next().split("#")[0].strip()
    body = _Body(name, [lines.number() for _ in range(6)])
    lines.number()  # total mass, which SIMA keeps on its model and not in the tree
    for names in (body.specified_forces, body.specified_moments, body.external_forces,
                  body.positioning_elements, body.thrusters, []):  # [] is slender elements
        names.extend(lines.next() for _ in range(lines.integer()))
    for _ in range(lines.integer()):
        body.couplings.append(lines.next())
        lines.next()  # the coupling
        lines.next()  # the branch
    if major > 2:
        for _ in range(lines.integer()):
            lines.next()  # stored elements
    return body


def _read_units(lines: _Lines) -> dict[str, str]:
    """``ResultUnitMapper.readUnits``: ``F=kN`` lines, base unit symbol to label."""
    units = {}
    for _ in range(lines.integer()):
        symbol, _, label = lines.next().partition("=")
        symbol, label = symbol.strip(), label.strip()
        group = SIMA_UNITS.get(symbol)
        if group is None or (label != group[0] and label not in group[1]):
            raise lines.error(f"unknown unit {symbol}={label}")
        units[group[0]] = label
    return units


# -- psc.lis: StaticConditionResultFactory ------------------------------------


@dataclass
class _Force:
    """``ForceResult``, in base units."""

    name: str
    fx: float
    fy: float
    fz: float
    mx: float
    my: float
    mz: float

    @property
    def ftotal(self) -> float:
        """``ForceResultImpl.getFtotal``."""
        return math.sqrt(self.fx * self.fx + self.fy * self.fy + self.fz * self.fz)


@dataclass
class _BodyResult:
    """``BodyResult``: one body's block, its containers in tree order."""

    name: str
    initial: list[float]
    static: list[float]
    body_forces: list[_Force]
    others: list[_Force]


def _read_psc(path: Path, mapper: _Mapper) -> list[_BodyResult]:
    lines = _Lines(path, "latin-1")
    for _ in range(3):
        lines.next()  # header, date tag, file part
    return [_read_body(lines, mapper) for _ in range(lines.integer())]


def _read_body(lines: _Lines, mapper: _Mapper) -> _BodyResult:
    index = lines.integer()
    short_id = lines.next().strip()
    if not 1 <= index <= len(mapper.bodies):
        raise lines.error(f"There is no result for the body {short_id}. "
                          f"This body does not exist in {MAPPER_FILENAME}")
    body = mapper.bodies[index - 1]
    static = lines.numbers(6, "the position")
    counts = _read_counts(lines)
    body_forces = _read_body_forces(lines)
    others = _read_elements(lines, body, counts)

    force, moment = mapper.scale(FORCE), mapper.scale(MOMENT)
    length, angle = mapper.scale(LENGTH), mapper.scale(ANGLE)
    position = (length, length, length, angle, angle, angle)
    return _BodyResult(
        name=body.name,
        initial=[scale * value for scale, value in zip(position, body.initial)],
        static=[scale * value for scale, value in zip(position, static)],
        body_forces=[_scaled(f, force, moment) for f in body_forces],
        others=[_scaled(f, force, moment) for f in others],
    )


def _read_counts(lines: _Lines) -> list[int]:
    """NELM, NCPL, NTHR, NGLIN, NSPF, NXFO."""
    counts = lines.next().split()
    try:
        if len(counts) == 6:
            return [int(count) for count in counts]
    except ValueError:
        pass
    raise lines.error("the force counts should be 6 integers")


def _read_body_forces(lines: _Lines) -> list[_Force]:
    count = lines.integer()
    if count > len(_BODY_FORCES):
        raise lines.error(f"{count} body forces, but SIMO defines {len(_BODY_FORCES)}")
    forces = []
    for name in _BODY_FORCES[:count]:
        values = lines.numbers(6, "a body force")
        if name != _VACANT:
            forces.append(_Force(name, *values))
    return forces


def _read_elements(lines: _Lines, body: _Body, counts: list[int]) -> list[_Force]:
    """Every element row, in PSCMetaDataImporter's order rather than the file's."""
    nelm, ncpl, nthr, _nglin, nspf, nxfo = counts
    positioning = [_element(lines, _name(body.positioning_elements, i, f"UNKNOWN_POS_ELEM_{i + 1}"))
                   for i in range(nelm)]
    couplings = []
    for i in range(ncpl):
        values = lines.numbers(7, "a coupling force")
        if i >= len(body.couplings):
            raise lines.error(f"Found unmatched coupling result {i} on body {body.name}")
        couplings.append(_Force(body.couplings[i], *values[1:]))
    thrusters = [_element(lines, _name(body.thrusters, i, f"UNKNOWN_THRUSTER_{i}"))
                 for i in range(nthr)]
    # General line forces are counted but never read, as in SIMA.
    expected = len(body.specified_forces) + len(body.specified_moments)
    if nspf != expected:
        raise lines.error(f"{nspf} specified forces on body {body.name}, "
                          f"but {MAPPER_FILENAME} names {expected}")
    specified = [_element(lines, name) for name in body.specified_forces + body.specified_moments]
    external = [_element(lines, _name(body.external_forces, i, f"UNKNOWN_EXTERNAL_{i}"))
                for i in range(nxfo)]
    return positioning + couplings + external + specified + thrusters


def _element(lines: _Lines, name: str) -> _Force:
    """A 7-value row: the total, which SIMA recomputes, then the six components."""
    return _Force(name, *lines.numbers(7, "an element force")[1:])


def _name(names: list[str], index: int, fallback: str) -> str:
    return names[index] if index < len(names) else fallback


def _scaled(f: _Force, force: float, moment: float) -> _Force:
    return _Force(f.name, force * f.fx, force * f.fy, force * f.fz,
                  moment * f.mx, moment * f.my, moment * f.mz)


# -- the tree: PSCMetaDataImporter --------------------------------------------


def _add_body(into: Container, result: _BodyResult) -> None:
    body = get_or_create_child(into, result.name)
    set_attribute(body, BODY, result.name)
    set_type(body, BODY)
    for name, values in (("Initial position", result.initial), ("Static position", result.static)):
        container = graft(body, Container(name))
        for signal, unit, value in zip(("x", "y", "z", "rx", "ry", "rz"),
                                       (LENGTH,) * 3 + (ANGLE,) * 3, values):
            _add(container, signal, value, unit, result.name)
    for f in result.body_forces:
        _add_force(body, f, result.name, (("Fx", FORCE, f.fx), ("Fy", FORCE, f.fy),
                                          ("Fz", FORCE, f.fz), ("FTotal", FORCE, f.ftotal)))
    for f in result.others:
        _add_force(body, f, result.name, (("FTotal", FORCE, f.ftotal), ("Fx", FORCE, f.fx),
                                          ("Fy", FORCE, f.fy), ("Fz", FORCE, f.fz)))


def _add_force(body: Container, f: _Force, body_name: str,
               forces: tuple[tuple[str, str, float], ...]) -> None:
    container = graft(body, Container(f.name))
    for name, unit, value in forces + (("Mx", MOMENT, f.mx), ("My", MOMENT, f.my),
                                       ("Mz", MOMENT, f.mz)):
        _add(container, name, value, unit, body_name)


def _add(container: Container, name: str, value: float, unit: str, body: str) -> None:
    add_signal(container, constant(name, value, unit=unit, xunit=NONDIMENSIONAL, **{BODY: body}))


@register
class PscReader:  # pylint: disable=too-few-public-methods
    """``psc.lis``, or ``psc-sima.lis`` from a RIFLEX-coupled run."""

    types: ClassVar[frozenset[str]] = frozenset()
    names: ClassVar[frozenset[str]] = frozenset({"psc.lis", "psc-sima.lis"})

    def read(self, source: Source, into: Container) -> None:
        """Read one ``psc.lis`` into a fresh container. See ``Reader.read``.

        :raises SourceError: if ``simores.inp`` is missing or either file is malformed.
        """
        mapper_path = source.path.parent / MAPPER_FILENAME
        if not mapper_path.is_file():
            raise SourceError(
                f"no {MAPPER_FILENAME} beside {source.file}: it names the bodies and "
                f"elements {source.file} only numbers, and SIMA writes it with every static run"
            )
        for result in _read_psc(source.path, _read_mapper(mapper_path)):
            _add_body(into, result)

"""Unit labels to SIMA's base units, with the factor the values need.

A port of SIMA's unit machinery in three pieces: the registry of base units
and the alternative labels that convert into each (:data:`SIMA_UNITS`), the
label grammar (:func:`parse` and :func:`format_units`), and the per-atom
resolution (:func:`base_unit` and :func:`unit_factor`).

A solver writes values in the units its labels declare (``[kN]``); results are
reported in base units, so a kN value becomes N by **dividing** by the unit's
factor. A factor is what to multiply the base unit by to get the labelled one,
so ``kN`` is ``0.001`` and ``value_base = value_label / factor``.

**Resolution is per atom, never per compound.** ``kN/m^2`` is decomposed to
``{kN: 1, m: -2}``, each atom mapped to its group's base unit, and the result
recomposed. That is why no list of compound units appears here, and why
``kN*m/deg`` or ``MPa/foot`` work without being anticipated.

**An atom in no group resolves to** ``?``, and the signal is marked twice so the
values cannot be used unaware: :data:`UNSCALED_ATTRIBUTE` on the signal, and a
warning the first time the affected axis is read. Rescaling by a guess would be
worse than an honest unscaled number, but silence would be worse than either.

Three edge cases resolve differently here than in SIMA, each because SIMA's
answer is unusable rather than merely different:

* **Whitespace.** ``" mm"`` is trimmed once, consistently, so it keeps its
  factor of ``1000.0`` rather than resolving to metres unscaled.
* **Exponents that collide.** Two atoms sharing a base sum their exponents, so
  ``kN*MN`` is ``N^2``.
* **Empty atoms.** An atom of ``""`` -- reachable from ``m**2``, which the
  grammar does not support -- resolves to ``?`` instead of failing.
"""

from __future__ import annotations

import math
import re
from typing import Any

import numpy as np

from ._sources import warn

#: Base unit symbol -> (base label, {alternative label: factor}), as SIMA
#: registers them. The factor is how many of the alternative make one base unit, so
#: ``value_base = value_label / factor``.
#:
#: ``tonne`` is a **force** -- a tonne-force, ~9806.65 N -- not a mass. ``deg``
#: and ``rad`` are separate base units, so neither converts into the other, and
#: nor does ``kn``, which is not treated as a speed.
SIMA_UNITS: dict[str, tuple[str, dict[str, float]]] = {
    "F": ("N", {"kN": 0.001, "MN": 1.0e-6, "tonne": 0.001 / 9.80665}),
    "L": ("m", {"cm": 1.0e2, "mm": 1.0e3, "foot": 3.2808399}),
    "M": ("kg", {"g": 1e3, "Mg": 0.001, "Gg": 1.0e-6, "lbs": 2.20462262}),
    "P": ("Pa", {"kPa": 0.001, "MPa": 1.0e-6}),
    "W": ("W", {"kW": 0.001, "MW": 1.0e-6}),
    "T": ("s", {}),
    "H": ("h", {}),
    "TEMP": ("C", {}),
    "R": ("deg", {}),
    "RAD": ("rad", {}),
    "kn": ("kn", {}),
    "Y": ("year", {}),
    "RPM": ("rpm", {}),
    "Hz": ("Hz", {}),
    "1": ("1", {}),
    "-": ("-", {}),
    "?": ("unit unknown", {}),
    "%": ("%", {}),
}

#: What an atom in no group resolves to. ``findBaseUnitFromLabel`` returns this
#: rather than failing, and ``?`` is itself a registered symbol.
UNKNOWN_BASE = "?"


def _label_index() -> dict[str, tuple[str, float]]:
    """Flatten the registry to ``label -> (base label, factor)``.

    A base unit registers itself under its own label with factor 1.0, which is
    what ``BaseUnit``'s constructor does.
    """
    index: dict[str, tuple[str, float]] = {}
    for base, alternatives in SIMA_UNITS.values():
        index[base] = (base, 1.0)
        for label, factor in alternatives.items():
            index[label] = (base, factor)
    return index


#: Every label SIMA knows, to its base unit and factor.
_BY_LABEL = _label_index()

#: RIFLEX writes these symbolic prefixes instead of units; they are substituted
#: first, in this order. Matched on word boundaries, so a label merely
#: containing the letters -- ``MODULUS`` -- is left alone.
_PLACEHOLDERS = (("UF", "kN"), ("UL", "m"), ("UT", "s"), ("UM", "Mg"))
_PLACEHOLDER_RE = re.compile(r"\b(" + "|".join(p for p, _ in _PLACEHOLDERS) + r")\b")
_PLACEHOLDER_MAP = dict(_PLACEHOLDERS)

#: Labels the grammar cannot parse, which SIMA special-cases too. ``kN/(m*m)``
#: decomposes to the literal atoms ``(m`` and ``m)``, since parentheses are not
#: part of the grammar.
_UNPARSEABLE = {"kN/(m*m)": "kN/m^2"}

#: An expression, as ``{atom: exponent}`` in first-seen order. The printer
#: depends on that order, so a plain dict is load-bearing here.
Expression = dict[str, float]


def normalise(unit: str) -> str:
    """Trim, expand RIFLEX placeholders and fix the one unparseable spelling, as SIMA does."""
    text = unit.strip()
    text = _PLACEHOLDER_RE.sub(lambda match: _PLACEHOLDER_MAP[match.group(1)], text)
    return _UNPARSEABLE.get(text, text)


def parse(expression: str) -> Expression:
    """Decompose a label into atoms and exponents.

    The grammar checks ``/`` first, then ``*``, then ``^`` -- so **the divisor
    is everything after the first slash**, and ``a/b*c`` means ``a/(b*c)``.
    That is inverted from ordinary precedence and is deliberate: it is what SIMA
    does, and a label resolved any other way would disagree with SIMA on labels
    SIMA defines. Parentheses and ``**`` are not part of the grammar.

    Atoms keep first-seen order; ``1`` and ``-`` are the empty expression.
    """
    if "/" in expression:
        head, tail = expression.split("/", 1)
        return _multiply(parse(head), _inverted(parse(tail)))
    if "*" in expression:
        head, tail = expression.split("*", 1)
        return _multiply(parse(head), parse(tail))
    if "^" in expression:
        head, tail = expression.split("^", 1)
        try:
            power = float(tail)
        except ValueError:
            # SIMA raises NumberFormatException here. An unreadable exponent is
            # a label we cannot resolve, not a reason to lose the whole file.
            return {expression: 1.0}
        return {atom: exponent * power for atom, exponent in parse(head).items()}
    if expression in ("1", "-"):
        return {}
    return {expression: 1.0}


def _multiply(left: Expression, right: Expression) -> Expression:
    """Add the exponents of matching atoms."""
    result = dict(left)
    for atom, exponent in right.items():
        result[atom] = result.get(atom, 0.0) + exponent
    return result


def _inverted(expression: Expression) -> Expression:
    return {atom: -exponent for atom, exponent in expression.items()}


def _formatted(atom: str, exponent: float) -> str:
    """One atom with its exponent. ``getFormattedExponentiation``.

    An exponent of 1 prints bare and an exponent of 0 prints nothing, which is
    how an atom that cancels disappears from the result.
    """
    if exponent == 1.0:
        return atom
    if exponent == 0.0:
        return ""
    if exponent.is_integer():
        return f"{atom}^{int(exponent)}"
    return f"{atom}^{exponent}"


def format_units(expression: Expression) -> str:
    """Render an expression back to a label.

    Positive exponents form the numerator and negative ones the denominator,
    each joined by ``*``. **The denominator is never parenthesised** -- SIMA
    prints ``1/A*B^2``, which is only self-consistent because its own parser
    gives ``/`` the lowest precedence. Nothing left prints ``-``.
    """
    numerator: list[str] = []
    denominator: list[str] = []
    for atom, exponent in expression.items():
        text = _formatted(atom, abs(exponent))
        if not text:
            continue
        (denominator if exponent < 0 else numerator).append(text)

    head = "*".join(numerator) if numerator else "1"
    tail = "/" + "*".join(denominator) if denominator else ""
    result = head + tail
    return "-" if result in ("", "1") else result


def _atom_base(atom: str) -> str:
    """The base unit an atom belongs to.

    Trimmed here, once. SIMA trims for the symbol lookup but not for the factor
    lookup, which is how ``" mm"`` gets the right unit and the wrong numbers.
    """
    known = _BY_LABEL.get(atom.strip())
    return known[0] if known else UNKNOWN_BASE


def _atom_factor(atom: str) -> float:
    """An atom's factor.

    A label its base unit does not know falls back to 1.0 rather than failing,
    which is why SIMA gives ``kNdeg`` a factor of 1.0 rather than an error.
    """
    known = _BY_LABEL.get(atom.strip())
    return known[1] if known else 1.0


def base_unit(unit: str | None) -> str | None:
    """The label SIMA would report for this one; None for a missing or blank label."""
    if not unit or not unit.strip():
        return None
    text = normalise(unit)
    if text == "-":
        return "-"
    resolved: Expression = {}
    for atom, exponent in parse(text).items():
        base = _atom_base(atom)
        resolved[base] = resolved.get(base, 0.0) + exponent
    return format_units(resolved)


def unit_factor(unit: str | None) -> float:
    """What to divide values by to reach the base unit. ``getUnitFactorWithOperators``."""
    if not unit or not unit.strip():
        return 1.0
    text = normalise(unit)
    if text == "-":
        return 1.0
    factor = 1.0
    for atom, exponent in parse(text).items():
        factor *= _atom_factor(atom) ** exponent
    return factor


#: Base units that measure the same thing, as ``base unit -> (label, factor)``
#: where one of the base unit is ``factor`` of the label.
#:
#: SIMA keeps ``deg`` and ``rad`` -- and ``s`` and ``h`` -- as separate base
#: units so that reading a file can never silently turn one into the other.
#: This table changes nothing on the way in: only :func:`conversion_factor`
#: consults it, and that runs when a caller asks for a unit by name.
#:
#: Every factor here is exact by definition, which is the bar for the table.
#: ``year`` is absent because its length is a convention SIMA does not fix, and
#: ``C`` because it needs an offset rather than a factor.
BASE_BRIDGES: dict[str, tuple[str, float]] = {
    "rad": ("deg", 180.0 / math.pi),
    "h": ("s", 3600.0),
    "Hz": ("1/s", 1.0),
    "rpm": ("Hz", 1.0 / 60.0),
    "kn": ("m/s", 1852.0 / 3600.0),  # the international nautical mile
}


def _canonical(expression: Expression) -> tuple[Expression, float]:
    """An expression with every bridged atom rewritten, and the factor to it.

    Comparing two of these is how :func:`conversion_factor` decides whether two
    labels measure the same thing. Rewriting per atom is what makes it compose:
    ``rad/s`` and ``deg/h`` both reduce to ``deg/s``, so they are compatible,
    and the two factors say how far apart. A bridge may lead to another
    (``rpm`` to ``Hz`` to ``1/s``), so this folds until no bridged atom is left.
    """
    factor = 1.0
    while any(atom in BASE_BRIDGES for atom in expression):
        folded: Expression = {}
        for atom, exponent in expression.items():
            bridge = BASE_BRIDGES.get(atom)
            if bridge is None:
                folded[atom] = folded.get(atom, 0.0) + exponent
                continue
            label, scale = bridge
            factor *= scale**exponent
            for sub, sub_exponent in parse(label).items():
                folded[sub] = folded.get(sub, 0.0) + sub_exponent * exponent
        expression = folded
    return ({a: e for a, e in expression.items() if e != 0.0}, factor)


def conversion_factor(current: str | None, target: str) -> float:
    """What to multiply values labelled ``current`` by to label them ``target``.

    The opposite direction from :func:`unit_factor`, which says what to divide a
    file's values by on the way in. This is for going back out: values held in
    ``N`` presented as ``kN``.

    Chains safely -- the current label's own factor is divided out -- so
    converting twice is not scaling twice.

    :raises ValueError: if either label has no known conversion, or if the two
        measure different things. :data:`BASE_BRIDGES` lists the pairs SIMA's
        registry separates that are convertible anyway.
    """
    target_base = base_unit(target)
    if not is_mapped(target) or target_base is None or target_base == "-":
        raise ValueError(
            f"cannot convert to {target!r}: it is not a unit with a known "
            f"conversion."
        )
    if not current or not is_mapped(current):
        raise ValueError(
            f"cannot convert from {current!r} to {target!r}: the values carry "
            f"no unit that can be converted."
        )
    current_base = base_unit(current) or ""
    current_canonical, current_scale = _canonical(parse(current_base))
    target_canonical, target_scale = _canonical(parse(target_base))
    if current_canonical != target_canonical:
        raise ValueError(
            f"cannot convert {current!r} to {target!r}: they measure different "
            f"things ({current_base} and {target_base})."
        )
    return unit_factor(target) / unit_factor(current) * current_scale / target_scale


def map_unit(unit: str | None) -> tuple[str, float]:
    """Return ``(unit, factor)`` for a label. What the readers call.

    Differs from :func:`base_unit` in one way, deliberately. SIMA resolves an
    atom it does not know to ``?``, which is the honest answer to *"what is the
    base unit of this"* but a useless one to put on a signal: the values really
    are in kip, and a signal claiming ``?`` has lost that. So a label that
    cannot be fully resolved keeps **the label the file wrote**, and
    :func:`guard_unscaled` marks the signal so the numbers cannot be mistaken
    for base units. Callers wanting SIMA's own answer should ask
    :func:`base_unit`.

    ``value_base = value_label / factor``; a missing label is ``("", 1.0)``.
    """
    if unit is None:
        return ("", 1.0)
    if not is_mapped(unit):
        # Either fully resolve or touch nothing. Scaling the atoms we do know
        # while leaving the label alone would divide ``kN/glorp`` by 0.001 and
        # still call it kN -- values and label disagreeing is worse than both
        # being the file's own.
        return (normalise(unit), 1.0)
    return (base_unit(unit) or "", unit_factor(unit))


#: Set on a signal whose unit SIMA's registry does not know, to the label as
#: written. Present means the numbers are in the file's unit, not a base unit.
UNSCALED_ATTRIBUTE = "unscaled"


def is_mapped(unit: str | None) -> bool:
    """Whether every atom of this label is in SIMA's registry.

    True for a missing or blank label: nothing to scale is not a failure to scale.
    """
    if unit is None or not unit.strip():
        return True
    text = normalise(unit)
    if text == "-":
        return True
    atoms = parse(text)
    if not atoms:
        return True
    return all(atom.strip() in _BY_LABEL for atom in atoms)


class Unscaled:
    """Values whose unit SIMA's registry does not know, wrapped to say so.

    Forwards everything to the values it wraps -- including ``xstart`` and
    ``xdelta``, which :class:`~simapy_results.Signal` reads off the
    provider -- and warns once per axis the first time that axis is read.

    Once per axis, not once per call: a loop over a thousand signals should say
    so a thousand times, but reading one signal twice is not new information.
    """

    def __init__(self, values, where: str, unit: str | None = None,
                 xunit: str | None = None):
        self._values = values
        self._where = where
        self._unit = unit
        self._xunit = xunit
        self._warned: set[str] = set()

    @property
    def size(self) -> int:
        """Sample count, which needs no unit."""
        return self._values.size

    def x(self) -> np.ndarray:
        """The x values, in the file's own unit if that unit is unknown."""
        self._warn("xunit", self._xunit)
        return self._values.x()

    def y(self) -> np.ndarray:
        """The y values, in the file's own unit if that unit is unknown."""
        self._warn("unit", self._unit)
        return self._values.y()

    def _warn(self, axis: str, unit: str | None) -> None:
        if unit is None or axis in self._warned:
            return
        self._warned.add(axis)
        warn(
            f"{self._where}: {axis} {unit!r} is not in SIMA's unit registry, so "
            f"these values are in {unit!r} and not a base unit."
        )

    def __getattr__(self, name: str) -> Any:
        # Reached for _values itself only before __init__ has run, as in copy.copy.
        if name == "_values":
            raise AttributeError(name)
        return getattr(self._values, name)


def unscaled_units(unit: str | None, xunit: str | None = None) -> dict[str, str]:
    """Which of these labels cannot be scaled, as ``{axis: label}``."""
    unknown = {}
    if unit is not None and not is_mapped(unit):
        unknown["unit"] = unit
    if xunit is not None and not is_mapped(xunit):
        unknown["xunit"] = xunit
    return unknown


def guard_unscaled(values, where: str, unit: str | None = None,
                   xunit: str | None = None) -> tuple[Any, dict[str, str]]:
    """Wrap values and tag the signal when either unit label is unknown.

    Returns ``(values, attributes)``: the values unchanged and no attributes
    when both labels are known, else wrapped in :class:`Unscaled` with
    :data:`UNSCALED_ATTRIBUTE` set. ``where`` names the signal in the warning.
    """
    unknown = unscaled_units(unit, xunit)
    if not unknown:
        return values, {}
    marker = ", ".join(f"{axis}={label}" for axis, label in unknown.items())
    wrapped = Unscaled(values, where, unknown.get("unit"), unknown.get("xunit"))
    return wrapped, {UNSCALED_ATTRIBUTE: marker}

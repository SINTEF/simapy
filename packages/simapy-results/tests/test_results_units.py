"""Unit labels to SIMA's base units.

**These are SIMA's own assertions.** Every expected value marked
``UnitUtilTest.java:N`` is copied from that line of sima-platform's
``no.marintek.sima.model/src-test/.../UnitUtilTest.java``, case for case. So a
pass there is conformance with SIMA, not this port agreeing with itself.

Where the port deliberately differs from SIMA, the test says so and says why --
those are the three cases in ``TestDeliberateDivergences``, each a place SIMA
produces the right unit with the wrong numbers, or raises.
"""

import warnings

import pytest

from simapy_results import Signal
from simapy_results._units import (
    BASE_BRIDGES,
    SIMA_UNITS,
    UNSCALED_ATTRIBUTE,
    base_unit,
    conversion_factor,
    format_units,
    guard_unscaled,
    is_mapped,
    map_unit,
    normalise,
    parse,
    unit_factor,
)

from .conftest import ArrayValues


class TestRegistry:
    """The registry data, transcribed from SIMA."""

    def test_holds_every_base_unit(self):
        assert len(SIMA_UNITS) == 18

    def test_holds_every_alternative_label(self):
        assert sum(len(alts) for _, alts in SIMA_UNITS.values()) == 14

    def test_a_tonne_is_a_force_not_a_mass(self):
        """The line most likely to be got wrong: SIMA's tonne is tonne-force."""
        assert base_unit("tonne") == "N"
        assert unit_factor("tonne") == pytest.approx(0.001 / 9.80665)
        assert 1.0 / unit_factor("tonne") == pytest.approx(9806.65)

    def test_degrees_and_radians_are_separate_base_units(self):
        """SIMA registers R->deg and RAD->rad, so neither converts."""
        assert (base_unit("deg"), unit_factor("deg")) == ("deg", 1.0)
        assert (base_unit("rad"), unit_factor("rad")) == ("rad", 1.0)
        assert base_unit("deg/s^2") == "deg/s^2"
        assert unit_factor("rad/s") == 1.0


class TestParser:
    """The label grammar, including the parts that surprise."""

    def test_the_divisor_is_everything_after_the_first_slash(self):
        """`/` binds loosest, so a/b*c is a/(b*c). Inverted from maths, and
        deliberate -- SIMA splits and inverts the whole
        right-hand side."""
        assert parse("a/b*c") == {"a": 1.0, "b": -1.0, "c": -1.0}

    def test_one_and_dash_are_the_empty_expression(self):
        """How a divisor is parsed."""
        assert parse("1") == {}
        assert parse("-") == {}

    def test_exponents_multiply_the_whole_left_side(self):
        assert parse("kN*m^2") == {"kN": 1.0, "m": 2.0}
        assert parse("1/m") == {"m": -1.0}
        assert parse("kN/m^2") == {"kN": 1.0, "m": -2.0}

    def test_repeated_atoms_sum(self):
        assert parse("m*m") == {"m": 2.0}
        assert parse("m/m") == {"m": 0.0}

    def test_parentheses_are_not_in_the_grammar(self):
        """They become part of the atom names, which is why SIMA hard-codes
        kN/(m*m) rather than parsing it."""
        assert parse("kN/(m*m)") == {"kN": 1.0, "(m": -1.0, "m)": -1.0}

    def test_the_one_unparseable_label_is_rewritten_before_parsing(self):
        assert normalise("kN/(m*m)") == "kN/m^2"
        assert base_unit("kN/(m*m)") == "N/m^2"
        assert unit_factor("kN/(m*m)") == pytest.approx(0.001)


class TestPrinter:
    """Rendering an expression back to a label."""

    def test_an_atom_that_cancels_disappears(self):
        assert format_units({"m": 0.0}) == "-"
        assert format_units({"N": 1.0, "m": 0.0}) == "N"

    def test_the_denominator_is_not_parenthesised(self):
        """SIMA prints 1/A*B^2, which only its own parser reads back correctly."""
        assert format_units({"A": -1.0, "B": -2.0}) == "1/A*B^2"
        assert parse(format_units({"A": -1.0, "B": -2.0})) == {"A": -1.0, "B": -2.0}


class TestFactor:
    """The factor for a whole label. Every case SIMA's own tests cover."""

    @pytest.mark.parametrize("label, expected", [
        (None, 1.0),                            # UnitUtilTest.java:52
        ("", 1.0),                              # UnitUtilTest.java:53
        ("-", 1.0),                             # UnitUtilTest.java:54
        ("1/kN", 1000.0),                       # UnitUtilTest.java:55
        ("1*s", 1.0),                           # UnitUtilTest.java:56
        ("1*kN", 0.001),                        # UnitUtilTest.java:57
        ("1*N", 1.0),                           # UnitUtilTest.java:58
        ("mm", 1000.0),                         # UnitUtilTest.java:59
        ("1/mm", 1 / 1000.0),                   # UnitUtilTest.java:60
        ("cm", 100.0),                          # UnitUtilTest.java:61
        ("1/cm", 1 / 100.0),                    # UnitUtilTest.java:62
        ("g/kW*h", 1000.0 * 1000.0),            # UnitUtilTest.java:63
        ("kNdeg", 1.0),                         # UnitUtilTest.java:84  one unknown atom
        ("kN*bogus", 0.001),                    # UnitUtilTest.java:85  unknown atom is 1.0
    ])
    def test_factor(self, label, expected):
        assert unit_factor(label) == pytest.approx(expected)


class TestBaseUnit:
    """The base unit for a whole label. Every case SIMA's own tests cover."""

    @pytest.mark.parametrize("label, expected", [
        ("", None),                             # UnitUtilTest.java:68
        (None, None),                           # UnitUtilTest.java:69
        ("-", "-"),                             # UnitUtilTest.java:70
        ("1/kN", "1/N"),                        # UnitUtilTest.java:71
        ("1*s", "s"),                           # UnitUtilTest.java:72
        ("1*kN", "N"),                          # UnitUtilTest.java:73
        ("1*N", "N"),                           # UnitUtilTest.java:74
        ("1/bogus", "1/?"),                     # UnitUtilTest.java:79  unknown atom becomes ?
    ])
    def test_base_unit(self, label, expected):
        assert base_unit(label) == expected


class TestAlternativeLabels:
    """Labels beyond N, m, s and kg, each resolving to its group's base unit."""

    @pytest.mark.parametrize("label, unit, factor", [
        ("Mg", "kg", 0.001),
        ("g", "kg", 1e3),
        ("Gg", "kg", 1.0e-6),
        ("lbs", "kg", 2.20462262),
        ("cm", "m", 1.0e2),
        ("mm", "m", 1.0e3),
        ("foot", "m", 3.2808399),
        ("MN", "N", 1.0e-6),
        ("kPa", "Pa", 0.001),
        ("MPa", "Pa", 1.0e-6),
        ("kW", "W", 0.001),
        ("MW", "W", 1.0e-6),
        ("Hz", "Hz", 1.0),
        ("rpm", "rpm", 1.0),
        ("h", "h", 1.0),
        ("%", "%", 1.0),
        ("kn", "kn", 1.0),
    ])
    def test_resolves_to_its_base_unit(self, label, unit, factor):
        assert map_unit(label) == (unit, pytest.approx(factor))
        assert is_mapped(label)

    def test_a_compound_of_them_composes(self):
        """No compound is enumerated anywhere, so this has to fall out."""
        assert base_unit("MPa/foot") == "Pa/m"
        assert base_unit("kN*m/deg") == "N*m/deg"
        assert unit_factor("kN*m/deg") == pytest.approx(0.001)


class TestPlaceholders:
    """RIFLEX's symbolic prefixes."""

    @pytest.mark.parametrize("label, expected", [
        ("UF", "N"),
        ("UL", "m"),
        ("UT", "s"),
        ("UM", "kg"),
        ("UF/UL^2", "N/m^2"),
    ])
    def test_substituted_then_resolved(self, label, expected):
        assert base_unit(label) == expected

    def test_a_word_containing_a_placeholder_is_left_alone(self):
        """Deliberate divergence: SIMA's replaceAll turns MODULUS into MODmS."""
        assert normalise("MODULUS") == "MODULUS"


class TestWhatTheReadersSee:
    """map_unit's contract, which the readers depend on."""

    @pytest.mark.parametrize("label, expected", [
        ("kN", ("N", 0.001)),
        ("kN*m", ("N*m", 0.001)),
        ("kN/m", ("N/m", 0.001)),
        ("kN/m^2", ("N/m^2", 0.001)),
        ("kN/(m*m)", ("N/m^2", 0.001)),
        ("1/m", ("1/m", 1.0)),
        ("m", ("m", 1.0)),
        ("s", ("s", 1.0)),
        ("deg", ("deg", 1.0)),
        ("kg", ("kg", 1.0)),
        ("-", ("-", 1.0)),
        ("", ("", 1.0)),
        ("  ", ("", 1.0)),
        (None, ("", 1.0)),
    ])
    def test_the_label_and_factor_a_reader_applies(self, label, expected):
        unit, factor = map_unit(label)
        assert (unit, pytest.approx(factor)) == (expected[0], expected[1])

    def test_an_unknown_label_keeps_the_files_own_label_and_numbers(self):
        """SIMA would answer "?" -- true, but useless on a signal, because the
        values really are in glorp. base_unit still gives SIMA's answer."""
        assert map_unit("glorp") == ("glorp", 1.0)
        assert base_unit("glorp") == "?"
        assert not is_mapped("glorp")

    def test_a_compound_with_one_unknown_atom_scales_nothing(self):
        """Either fully resolve or touch nothing.

        Scaling the kN while leaving the label alone would divide by 0.001 and
        still call it kN -- values and label disagreeing is worse than both
        being the file's own. base_unit still answers as SIMA does.
        """
        assert not is_mapped("kN/glorp")
        assert map_unit("kN/glorp") == ("kN/glorp", 1.0)
        assert base_unit("kN/glorp") == "N/?"
        assert unit_factor("kN/glorp") == pytest.approx(0.001), "the raw factor"


class TestUnscaledMarking:
    """Only a label SIMA's registry does not know marks a signal unscaled."""

    @pytest.mark.parametrize("label", [None, "", "   "], ids=["none", "empty", "blank"])
    def test_no_unit_is_not_an_unknown_unit(self, label):
        values = ArrayValues([0.0, 1.0], [2.0, 3.0])

        guarded, attributes = guard_unscaled(values, "where", unit=label, xunit=label)

        assert guarded is values
        assert attributes == {}
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            assert list(Signal("s", guarded, unit=label, xunit=label).y) == [2.0, 3.0]

    def test_an_unknown_unit_is_marked_and_warns_once_per_axis(self):
        guarded, attributes = guard_unscaled(
            ArrayValues([0.0], [1.0]), "load", unit="kip", xunit="s"
        )

        assert attributes == {UNSCALED_ATTRIBUTE: "unit=kip"}
        with pytest.warns(UserWarning, match="'kip' is not in SIMA's unit registry"):
            guarded.y()
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            guarded.y()
            guarded.x()


class TestDeliberateDivergences:
    """Three places SIMA is wrong. Each is a choice, not an oversight."""

    def test_whitespace_in_an_atom_does_not_lose_the_factor(self):
        """SIMA trims when looking up the symbol but not when looking up
        BaseUnit.getUnit (BaseUnit:47), so it resolves " mm" to base m with
        factor 1.0 -- the right unit and the wrong numbers."""
        assert base_unit("1* mm") == "m"
        assert unit_factor("1* mm") == pytest.approx(1000.0), "SIMA gives 1.0"

    def test_exponents_sum_when_two_atoms_share_a_base(self):
        """SIMA overwrites rather than sums here, collapsing these to
        N instead of N^2."""
        assert base_unit("kN*MN") == "N^2", "SIMA gives N"

    def test_an_empty_atom_resolves_instead_of_raising(self):
        """m**2 is not in the grammar, so it parses as m * "" * 2, and both
        unknown atoms resolve to ?; SIMA raises NullPointerException while
        formatting."""
        assert base_unit("m**2") == "m*?^2"
        assert unit_factor("m**2") == pytest.approx(1.0)


class TestConversionFactor:
    """Going back out -- values held in a base unit, presented as something else.

    No Java to conform to: SIMA converts on the way in and never back, so these
    assertions are arithmetic, checked against each factor's definition.
    """

    @pytest.mark.parametrize(
        "current, target, expected",
        [
            ("N", "kN", 0.001),
            ("N", "MN", 1.0e-6),
            ("N", "tonne", 0.001 / 9.80665),
            ("m", "mm", 1000.0),
            ("m", "cm", 100.0),
            ("m", "foot", 3.2808399),
            ("kg", "Mg", 0.001),
            ("Pa", "MPa", 1.0e-6),
            ("W", "kW", 0.001),
        ],
    )
    def test_the_registry_factor_is_the_multiplier(self, current, target, expected):
        """A factor says how many of a label make one base unit, so presenting
        base values in that label is a multiplication by it."""
        assert conversion_factor(current, target) == pytest.approx(expected)

    def test_a_label_converts_to_itself_unchanged(self):
        assert conversion_factor("N", "N") == 1.0
        assert conversion_factor("deg", "deg") == 1.0

    def test_compounds_resolve_per_atom(self):
        """No compound is enumerated anywhere, so these work without being
        anticipated."""
        assert conversion_factor("N*m", "kN*m") == pytest.approx(0.001)
        assert conversion_factor("m/s^2", "mm/s^2") == pytest.approx(1000.0)
        assert conversion_factor("N/m", "kN/m") == pytest.approx(0.001)

    def test_converting_from_an_alternative_label_divides_its_factor_out(self):
        """So that ``to("kN").to("N")`` is the identity and not a second
        scaling."""
        assert conversion_factor("kN", "N") == pytest.approx(1000.0)
        assert conversion_factor("kN", "kN") == pytest.approx(1.0)
        assert conversion_factor("kN", "MN") == pytest.approx(0.001)
        assert conversion_factor("mm", "m") == pytest.approx(0.001)


class TestBridgedBaseUnits:
    """The pairs SIMA's registry separates that convert anyway.

    SIMA gives deg and rad -- and s and h -- separate base units so that reading
    a file can never swap them silently. That holds: nothing about reading
    consults BASE_BRIDGES. But a caller naming one has asked, and refusing on
    the grounds that seconds and hours "measure different things" would be
    indefensible.
    """

    @pytest.mark.parametrize(
        "current, target, expected",
        [
            ("deg", "rad", 0.017453292519943295),  # pi/180
            ("rad", "deg", 57.29577951308232),  # 180/pi
            ("s", "h", 1.0 / 3600.0),
            ("h", "s", 3600.0),
            ("Hz", "rpm", 60.0),
            ("rpm", "Hz", 1.0 / 60.0),
            ("Hz", "1/s", 1.0),
            ("1/s", "Hz", 1.0),
            ("rpm", "1/s", 1.0 / 60.0),
            ("1/s", "rpm", 60.0),
            ("kn", "m/s", 1852.0 / 3600.0),  # international nautical mile
            ("m/s", "kn", 3600.0 / 1852.0),
        ],
    )
    def test_each_bridge_both_ways(self, current, target, expected):
        assert conversion_factor(current, target) == pytest.approx(expected)

    def test_a_bridge_composes_inside_a_compound(self):
        """Rewriting per atom, like everything else here, so these need no
        entry of their own: rad/s and deg/h both reduce to deg/s."""
        assert conversion_factor("deg/s^2", "rad/s^2") == pytest.approx(
            0.017453292519943295
        )
        assert conversion_factor("rad/s", "deg/h") == pytest.approx(
            57.29577951308232 * 3600.0
        )
        assert conversion_factor("m/s", "m/h") == pytest.approx(3600.0)
        assert conversion_factor("deg^2", "rad^2") == pytest.approx(
            0.017453292519943295**2
        )
        assert conversion_factor("m*Hz", "m/h") == pytest.approx(3600.0)

    def test_reading_a_file_never_consults_a_bridge(self):
        """The constraint the split exists for. deg stays deg and s stays s, so
        no value changes on the way in."""
        assert map_unit("deg") == ("deg", 1.0)
        assert map_unit("rad") == ("rad", 1.0)
        assert map_unit("s") == ("s", 1.0)
        assert map_unit("deg/s^2") == ("deg/s^2", 1.0)
        assert map_unit("Hz") == ("Hz", 1.0)
        assert base_unit("rad") == "rad", "resolving rad must not reach deg"
        assert base_unit("h") == "h"

    def test_year_and_celsius_are_deliberately_not_bridged(self):
        """A year is 365 days, or 365.25, or 365.2425 -- SIMA does not say, and
        a convention chosen here would be invisible in the result. Celsius is an
        offset rather than a factor, with no kelvin to offset to."""
        assert "year" not in BASE_BRIDGES
        assert "C" not in BASE_BRIDGES
        with pytest.raises(ValueError, match="measure different things"):
            conversion_factor("s", "year")
        with pytest.raises(ValueError, match="measure different things"):
            conversion_factor("C", "s")


class TestConversionRefusals:
    """What cannot be converted, and why the message says so."""

    def test_different_quantities_are_refused(self):
        with pytest.raises(ValueError, match="measure different things"):
            conversion_factor("N", "m")
        with pytest.raises(ValueError, match="measure different things"):
            conversion_factor("deg", "m")

    def test_pressure_is_its_own_quantity_in_simas_registry(self):
        """Not a defect here. SIMA holds Pa as a base unit unrelated to force
        over area, so bridging it would put simapy's answer at odds with the
        one SIMA shows."""
        assert base_unit("kPa") == "Pa"
        assert base_unit("N/m^2") == "N/m^2"
        with pytest.raises(ValueError, match="measure different things"):
            conversion_factor("N/m^2", "kPa")

    def test_an_unknown_target_is_refused(self):
        with pytest.raises(ValueError, match="not a unit with a known conversion"):
            conversion_factor("N", "glorp")

    def test_an_unresolved_source_cannot_be_converted(self):
        """A label that could not be resolved on the way in has values in the
        file's own unit, so there is nothing to convert from."""
        with pytest.raises(ValueError, match="no unit that can be converted"):
            conversion_factor("glorp", "N")
        with pytest.raises(ValueError, match="no unit that can be converted"):
            conversion_factor("kN/glorp", "kN")

    def test_a_missing_unit_is_refused_rather_than_assumed(self):
        for absent in (None, ""):
            with pytest.raises(ValueError, match="no unit that can be converted"):
                conversion_factor(absent, "kN")

    def test_dimensionless_converts_to_nothing(self):
        with pytest.raises(ValueError):
            conversion_factor("-", "kN")
        with pytest.raises(ValueError, match="not a unit with a known conversion"):
            conversion_factor("N", "-")

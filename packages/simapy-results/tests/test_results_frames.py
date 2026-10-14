"""pandas views over the tree. numpy stays the core; these are convenience."""

import re

import numpy as np
import pytest

from simapy_results import open_results, signals_to_frame

from .conftest import DATA, array_signal

pytest.importorskip("pandas")

RUN = DATA / "Simple_Flexible_Riser" / "Initial"

CURVATURES = "Initial/Static/RiserLine/Static curvatures"
MOMENTS = "Initial/Dynamic/RiserLine/Moment envelope curves"
TENSION = "Initial/Static/RiserLine/Static forces/EFF. TENSION"


def test_a_container_is_the_natural_frame():
    frame = open_results(RUN)[CURVATURES].to_dataframe()

    assert list(frame.columns) == ["CY", "CZ", "CTOT"]
    assert frame.shape == (130, 3)
    assert frame.index.name == "m"
    assert frame["CY"].iloc[0] == pytest.approx(-0.1334)


def test_signals_in_a_container_share_an_axis_so_the_frame_is_dense():
    frame = open_results(RUN)[MOMENTS].to_dataframe()

    assert frame.shape == (130, 5)
    assert not frame.isna().any().any()


def test_units_ride_along_on_attrs():
    frame = open_results(RUN)[CURVATURES].to_dataframe()

    assert frame.attrs["units"] == {"CY": "1/m", "CZ": "1/m", "CTOT": "1/m"}
    assert frame.attrs["xunit"] == "m"


def test_a_signal_becomes_a_series():
    series = open_results(RUN)[TENSION].to_series()

    assert series.name == "EFF. TENSION"
    assert series.index.name == "m"
    assert len(series) == 65
    assert series.iloc[0] == pytest.approx(183114.1)
    assert series.attrs["unit"] == "N"


def test_a_seconds_axis_is_named_time():
    signal = array_signal("force", np.arange(3.0), np.ones(3), xunit="s")
    assert signals_to_frame([signal]).index.name == "time"


# -- x-axes that repeat ----------------------------------------------------


def test_a_repeating_x_axis_is_kept_as_is():
    """Curvature is sampled at both ends of every element: x is [0, 2, 2, 4, 4...].

    That is real data, not a defect, so the index keeps the duplicates and .loc
    on one of them returns both rows.
    """
    frame = open_results(RUN)[CURVATURES].to_dataframe()

    assert list(frame.index[:5]) == [0.0, 2.0, 2.0, 4.0, 4.0]
    assert len(frame.loc[2.0]) == 2


def test_index_false_gives_positional_semantics():
    frame = open_results(RUN)[CURVATURES].to_dataframe(index=False)

    assert list(frame.columns) == ["m", "CY", "CZ", "CTOT"]
    assert list(frame.index) == list(range(130))


# -- one axis per frame ----------------------------------------------------


def test_differing_lengths_are_refused_not_guessed_at():
    """Aligning on a repeating x-axis would silently invent data."""
    short = array_signal("A", [0.0, 1.0], [1.0, 2.0])
    long = array_signal("B", np.arange(3.0), np.zeros(3))

    with pytest.raises(ValueError, match=re.escape(
        "'A' and 'B' do not share an x-axis (2 vs 3 samples). "
        "Frame each container separately."
    )):
        signals_to_frame([short, long])


def test_differing_x_values_of_one_length_are_refused():
    first = array_signal("A", [0.0, 1.0, 2.0], np.zeros(3))
    shifted = array_signal("B", [0.0, 1.0, 3.0], np.zeros(3))

    with pytest.raises(ValueError, match=re.escape(
        "'A' and 'B' do not share an x-axis (same 3 samples, different x values). "
        "Frame each container separately."
    )):
        signals_to_frame([first, shifted])


def test_a_mixed_subtree_is_refused():
    line = open_results(RUN)["Initial/Static/RiserLine"]

    assert not line.signals  # the line itself holds none
    with pytest.raises(ValueError, match="Frame each container separately"):
        line.to_dataframe(recursive=True)


def test_recursive_works_when_the_subtree_shares_an_axis():
    forces = open_results(RUN)["Initial/Static/RiserLine/Static forces"]

    frame = forces.to_dataframe(recursive=True)

    assert list(frame.columns) == ["EFF. TENSION"]


def test_an_empty_container_says_so():
    with pytest.raises(ValueError, match="no signals"):
        open_results(RUN)["Initial/Static/RiserLine"].to_dataframe()


# -- column names ----------------------------------------------------------


def test_duplicate_names_are_suffixed_not_dropped():
    """The merge keeps same-named signals, so a frame must too, named as SIMA names them."""
    x = np.arange(3.0)
    signals = [array_signal("MY", x, np.zeros(3)), array_signal("MY", x, np.ones(3))]

    frame = signals_to_frame(signals)

    assert list(frame.columns) == ["MY", "MY_duplicate_1"]
    assert frame["MY_duplicate_1"].iloc[0] == 1.0


def test_names_set_the_columns_and_their_units():
    x = np.arange(3.0)
    signals = [
        array_signal("MY", x, np.zeros(3), unit="N*m"),
        array_signal("MY", x, np.ones(3), unit="kN*m"),
    ]

    frame = signals_to_frame(signals, names=["static", "dynamic"])

    assert list(frame.columns) == ["static", "dynamic"]
    assert frame.attrs["units"] == {"static": "N*m", "dynamic": "kN*m"}
    assert frame["dynamic"].iloc[0] == 1.0


@pytest.mark.parametrize("names", [["only one"], ["same", "same"]],
                         ids=["too-few", "repeated"])
def test_names_must_give_each_signal_its_own_column(names):
    x = np.arange(3.0)
    signals = [array_signal("A", x, np.zeros(3)), array_signal("B", x, np.ones(3))]

    with pytest.raises(ValueError, match="names must give each signal its own column"):
        signals_to_frame(signals, names=names)


# -- laziness --------------------------------------------------------------


def test_building_a_frame_is_what_reads_the_values(parses):
    container = open_results(RUN)[CURVATURES]
    assert parses == []

    container.to_dataframe()
    assert len(parses) == 1

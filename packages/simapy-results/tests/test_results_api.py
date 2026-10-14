"""Behaviour of the results API itself: laziness, merging, best-effort reading."""

import copy
import traceback
from pathlib import Path

import numpy as np
import pytest

from simapy_results import (
    Container,
    ErrorSignal,
    ResultsError,
    ResultSet,
    RunDescription,
    Signal,
    SourceError,
    Status,
    open_results,
)
from simapy_results import _scan as scan
from simapy_results._build import add_signal, graft, prune_empty, rename_duplicates, shallow_copy
from simapy_results._description import Entry, ResultFile
from simapy_results._importer import build_tree
from simapy_results._merge import merge_containers, merge_items
from simapy_results._node import constant
from simapy_results._registry import find_reader
from simapy_results._sources import FolderContext
from simapy_results._units import guard_unscaled

from .conftest import DATA, ArrayValues, array_signal

RUN = DATA / "Simple_Flexible_Riser" / "Initial"

TENSION = "Initial/Static/RiserLine/Static forces/EFF. TENSION"


# -- navigation ------------------------------------------------------------


def test_path_access_and_getitem_agree():
    res = open_results(RUN)
    stepwise = res["Initial"]["Static"]["RiserLine"]["Static forces"]["EFF. TENSION"]
    assert res[TENSION] is stepwise
    assert stepwise.path == TENSION


def test_true_names_survive():
    """The H5 stores 'EFF_ TENSION'; the mpf says 'EFF. TENSION' and so do we."""
    res = open_results(RUN)
    assert "EFF. TENSION" in res["Initial/Static/RiserLine/Static forces"].keys()


def test_an_empty_container_is_still_found():
    """A Container with no members is falsy, which `a or b` lookups skip."""
    root = Container("root")
    graft(root, Container("empty"))

    assert root["empty"].name == "empty"
    assert "empty" in root


def test_missing_key_names_the_alternatives():
    res = open_results(RUN)
    with pytest.raises(KeyError, match="Static"):
        res["Initial/Nope"]


def test_typed_accessors_narrow_what_getitem_cannot():
    """[] returns Any because the key decides the type; these do not."""
    res = open_results(RUN)

    assert res.signal(TENSION).unit == "N"
    assert res.container("Initial/Static").type == "static"

    with pytest.raises(TypeError, match="not a signal"):
        res.signal("Initial/Static")
    with pytest.raises(TypeError, match="not a container"):
        res.container(TENSION)


def test_an_empty_path_is_rejected():
    """An empty segment names nothing, so it is an error rather than this container."""
    res = open_results(RUN)

    with pytest.raises(KeyError, match="not a valid name or path"):
        res[""]
    with pytest.raises(KeyError, match="not a valid name or path"):
        res["Initial//Static"]


def test_descending_into_a_signal_says_so():
    res = open_results(RUN)

    with pytest.raises(KeyError, match="is a signal and has no members"):
        res[f"{TENSION}/deeper"]


def test_membership_of_a_non_string_is_false():
    res = open_results(RUN)

    assert 1 not in res
    assert None not in res


def test_same_named_siblings_are_renamed_as_sima_does():
    """SIMA's renameDuplicates numbering, over containers then signals, on the node itself."""
    root = Container("root")
    first = graft(root, Container("x"))
    second = graft(root, Container("x"))
    signal = add_signal(root, constant("x", 1.0))
    below = add_signal(second, constant("s", 2.0))

    rename_duplicates([root])

    assert [node.name for node in (first, second, signal)] == ["x", "x_duplicate_1", "x_duplicate_2"]
    assert root.keys() == ["x", "x_duplicate_1", "x_duplicate_2"]
    assert [c.name for c in root.containers] == ["x", "x_duplicate_1"]
    assert root.signal("x_duplicate_2") is signal
    assert below.path == "x_duplicate_1/s"
    for node in (first, second, signal, below):
        assert root[node.path] is node


def test_a_renamed_container_is_not_searched_for_duplicates():
    """SIMA skips a renamed item, so it never recurses into it."""
    root = Container("root")
    graft(root, Container("x"))
    second = graft(root, Container("x"))
    add_signal(second, constant("s", 1.0))
    add_signal(second, constant("s", 2.0))

    rename_duplicates([root])

    assert [s.name for s in second.signals] == ["s", "s"]


def test_an_opened_tree_has_its_duplicates_renamed():
    task = Container("Task", type="task")
    condition = graft(task, Container("C"))
    add_signal(condition, constant("F-MAX", 1.0))
    add_signal(condition, constant("F-MAX", 2.0))

    res = ResultSet(task, Path("."), RunDescription(task="Task", condition="C"), [])

    assert [s.name for s in res.run.signals] == ["F-MAX", "F-MAX_duplicate_1"]


def test_a_name_containing_a_slash_round_trips():
    """The longest child name the key starts with wins, so a slash in a name is not a level."""
    root = Container("root")
    plain = graft(root, Container("a"))
    slashed = graft(root, Container("a/b"))
    inner = add_signal(slashed, constant("c/d", 1.0))
    top = add_signal(root, constant("x/y", 2.0))

    assert inner.path == "a/b/c/d"
    assert root[inner.path] is inner
    assert root[top.path] is top
    assert root["a"] is plain
    assert root.select() == {"a/b/c/d": inner, "x/y": top}


def test_find_by_attribute():
    res = open_results(RUN)
    lines = res.find(type="line")
    assert [n.path for n in lines] == [
        "Initial/Static/RiserLine",
        "Initial/Dynamic/RiserLine",
    ]

    moments = res.find(unit="N*m")
    assert len(moments) == 14
    assert all(isinstance(n, Signal) for n in moments)


def test_signals_carry_their_line():
    res = open_results(RUN)
    assert res[TENSION].attributes["line"] == "RiserLine"


# -- the result set ----------------------------------------------------------


def test_run_is_the_condition_container():
    res = open_results(RUN)

    assert res.run is res["Initial"]
    assert res.run.type == "condition"


def test_a_relative_path_names_the_run_as_its_absolute_path_does(monkeypatch):
    monkeypatch.chdir(RUN)
    here = open_results(".")
    assert (here.name, here.run.name) == ("Simple_Flexible_Riser", "Initial")
    assert here.folder.samefile(RUN)

    monkeypatch.chdir(RUN.parent)
    assert open_results("Initial").run.name == "Initial"
    one_file = open_results(Path("Initial") / "sima_stamod.mpf")
    assert (one_file.name, one_file.run.name) == ("Simple_Flexible_Riser", "Initial")


def test_what_was_read_cannot_be_changed_through_the_result_set():
    res = open_results(RUN)

    assert isinstance(res.sources, tuple)
    with pytest.raises(AttributeError):
        res.folder = DATA
    with pytest.raises(AttributeError):
        res.description = None
    with pytest.raises(TypeError):
        res.description.variables["hs"] = None
    with pytest.raises(TypeError):
        res.description.names["Risea63d"] = "Other"


# -- laziness --------------------------------------------------------------


def test_metadata_does_not_parse_values(parses):
    res = open_results(RUN)
    signal = res[TENSION]
    assert (len(signal), signal.unit, signal.xunit) == (65, "N", "m")
    assert [n.name for n in res.walk()]  # full traversal
    assert parses == [], "structure pass must not touch a single number"

    assert signal.y[0] == pytest.approx(183114.1)
    assert len(parses) == 1


def test_a_block_is_parsed_once_for_all_its_signals(parses):
    curvatures = open_results(RUN)["Initial/Static/RiserLine/Static curvatures"]
    for name in ("CY", "CZ", "CTOT"):
        assert len(curvatures[name].y) == 130
    assert len(parses) == 1


def test_x_and_y_share_one_read(parses):
    signal = open_results(RUN)[TENSION]
    assert signal.x[0] == pytest.approx(1.0)
    assert len(signal.x) == len(signal.y) == len(signal)
    assert len(parses) == 1


# -- units -----------------------------------------------------------------


def test_kn_is_converted_to_newton():
    """The mpf says 1.831141E+002 kN; SIMA stores 183114.1 N."""
    signal = open_results(RUN)[TENSION]
    assert signal.unit == "N"
    assert signal.y[0] == pytest.approx(183114.1)


def test_dimensionless_units_pass_through():
    dnorm = open_results(RUN)["Initial/Static/Static convergence - Displacement norm"]
    assert dnorm["DNORM"].unit == "-"
    assert dnorm["DNORM"].attributes["yaxis.log"] == "true"


def test_unscaled_values_survive_a_copy():
    """copy builds the wrapper without __init__, so its forwarding must not recurse."""
    def unscaled():
        wrapped, marker = guard_unscaled(ArrayValues([0.0], [4.0]), "load", unit="kip")
        return wrapped, Signal("load", wrapped, unit="kip", **marker)

    with pytest.warns(UserWarning, match="kip"):
        assert copy.copy(unscaled()[0]).y()[0] == 4.0
    with pytest.warns(UserWarning, match="kip"):
        assert copy.deepcopy(unscaled()[1]).y[0] == 4.0


def test_a_failed_signal_raises_afresh_on_every_read():
    """Re-raising one stored exception would grow its traceback on each access."""
    cause = ValueError("bad row")
    error = SourceError("Unable to import result x.mpf")
    error.__cause__ = cause
    signal = ErrorSignal("broken", error)

    depths = []
    for _ in range(3):
        with pytest.raises(SourceError, match="Unable to import result") as raised:
            _ = signal.y
        assert raised.value is not error
        assert raised.value.__cause__ is cause
        depths.append(len(traceback.extract_tb(raised.value.__traceback__)))
    assert depths[0] == depths[1] == depths[2]


def test_warnings_point_at_the_callers_line(copy_run):
    left, right = Container("root"), Container("root")
    graft(left, Container("x", type="static"))
    graft(right, Container("x", type="dynamic"))
    with pytest.warns(UserWarning, match="disagree on type") as record:
        merge_containers(left, right)
    assert record[0].filename == __file__

    run = copy_run(RUN)
    (run / "sima_dynmod.mpf").write_text("MATRIX    truncated, line Risea63d\n")
    with pytest.warns(UserWarning, match="sima_dynmod.mpf") as record:
        open_results(run)
    assert record[0].filename == __file__

    wrapped, marker = guard_unscaled(ArrayValues([0.0], [1.0]), "load", unit="kip")
    with pytest.warns(UserWarning, match="kip") as record:
        _ = Signal("load", wrapped, unit="kip", **marker).y
    assert record[0].filename == __file__


def test_names_resolve_in_one_pass_longest_id_first():
    """A replaced name is never rewritten again by an id it happens to contain."""
    overlapping = FolderContext(folder=RUN, names={"Ab": "AbCd", "Cd": "X"})
    assert overlapping.resolve_names("Ab") == "AbCd"
    assert overlapping.resolve_names("line Ab / Cd") == "line AbCd / X"

    nested = FolderContext(folder=RUN, names={"Ab": "short", "Abc": "long"})
    assert nested.resolve_names("Abc") == "long"


# -- asking for a different unit -------------------------------------------


def test_to_presents_the_values_in_another_unit():
    """The mpf wrote kN and the reader stored N, so this is the round trip back
    to what the solver printed."""
    signal = open_results(RUN)[TENSION]
    assert signal.y[0] == pytest.approx(183114.1)
    assert signal.to("kN").y[0] == pytest.approx(183.1141)
    assert signal.to("kN").unit == "kN"
    assert signal.to("MN").y[0] == pytest.approx(0.1831141)


def test_to_leaves_the_original_alone():
    signal = open_results(RUN)[TENSION]
    converted = signal.to("kN")
    assert signal.unit == "N"
    assert signal.y[0] == pytest.approx(183114.1)
    assert converted is not signal


def test_converting_twice_is_not_scaling_twice():
    signal = open_results(RUN)[TENSION]
    back = signal.to("kN").to("N")
    assert back.unit == "N"
    assert back.y[0] == pytest.approx(signal.y[0])


def test_to_converts_the_x_axis_independently():
    signal = open_results(RUN)[TENSION]
    converted = signal.to(xunit="mm")
    assert converted.xunit == "mm"
    assert converted.unit == signal.unit, "y untouched"
    assert converted.x[-1] == pytest.approx(signal.x[-1] * 1000.0)
    assert np.array_equal(converted.y, signal.y)


def test_to_with_nothing_named_is_the_signal_itself():
    signal = open_results(RUN)[TENSION]
    assert signal.to() is signal


def test_to_keeps_a_constants_value_attribute_in_step():
    hs = constant("hs", 1.5, unit="m")

    in_mm = hs.to("mm")

    assert in_mm.y[0] == pytest.approx(1500.0)
    assert in_mm.attributes["value"] == "1500.0"
    assert hs.attributes["value"] == "1.5"


def test_a_converted_equidistant_axis_stays_equidistant():
    """xstart and xdelta are recomputed rather than forwarded. A signal whose
    start and step still read in seconds while its x() read hours would
    disagree with itself, and same_axis compares exactly those two numbers."""
    signal = _equidistant_force()
    converted = signal.to(xunit="h")
    assert converted.is_equidistant
    assert converted.xstart == pytest.approx(signal.xstart / 3600.0)
    assert converted.xdelta == pytest.approx(signal.xdelta / 3600.0)
    assert converted.x[-1] == pytest.approx(signal.x[-1] / 3600.0)
    assert not converted.same_axis(signal), "a rescaled axis is a different axis"


def test_to_does_not_read_the_values(parses):
    """Converting a signal nobody has looked at yet must stay lazy -- the whole
    tree is built without parsing, and .to() cannot be what breaks that."""
    converted = open_results(RUN)[TENSION].to("kN", xunit="mm")
    assert parses == [], "nothing read yet"
    assert converted.y[0] == pytest.approx(183.1141)
    assert len(parses) == 1, "and one read serves both axes"
    assert converted.x[0] == pytest.approx(1000.0)
    assert len(parses) == 1


def test_degrees_convert_to_radians_only_when_asked():
    """SIMA keeps deg and rad as separate base units so that reading a file
    cannot swap them. Reading holds to that; asking is a separate matter."""
    signal = _an_angle()
    assert signal.unit == "deg", "read as written"
    radians = signal.to("rad")
    assert radians.unit == "rad"
    assert radians.y[0] == pytest.approx(np.deg2rad(signal.y[0]))
    assert radians.to("deg").y[0] == pytest.approx(signal.y[0])


def test_to_refuses_a_unit_measuring_something_else():
    signal = open_results(RUN)[TENSION]
    with pytest.raises(ValueError, match="measure different things"):
        signal.to("m")
    with pytest.raises(ValueError, match="measure different things"):
        signal.to(xunit="kN")


def test_to_refuses_a_unit_sima_does_not_know():
    signal = open_results(RUN)[TENSION]
    with pytest.raises(ValueError, match="not a unit with a known conversion"):
        signal.to("kip")


def test_a_dimensionless_signal_cannot_be_given_a_unit():
    dnorm = open_results(RUN)["Initial/Static/Static convergence - Displacement norm"]
    with pytest.raises(ValueError):
        dnorm["DNORM"].to("kN")


HEAVY_LIFTING = DATA / "Heavy_Lifting_Operation" / "Initial"


def _equidistant_force():
    """A time series from the Heavy Lifting run, for the axis tests."""
    signal = open_results(HEAVY_LIFTING)[
        "Initial/Dynamic/Platform/Positioning elements/MooringLine1/Total force"
    ]
    assert signal.is_equidistant and signal.xunit == "s"
    return signal


def _an_angle():
    return open_results(HEAVY_LIFTING)[
        "Initial/Dynamic/Platform/Global total position/XB rotation"
    ]


# -- static load steps -----------------------------------------------------


def test_only_the_last_load_step_survives():
    """STAMOD writes steps 10, 210 and 220; SIMA keeps the last."""
    forces = open_results(RUN)["Initial/Static/RiserLine/Static forces"]
    assert forces.keys() == ["EFF. TENSION"]
    assert forces["EFF. TENSION"].y[0] == pytest.approx(183114.1)  # step 220


def test_dynamic_matrices_are_not_collapsed():
    """DYNMOD has no load steps, so every matrix keeps its own container."""
    dynamic = open_results(RUN)["Initial/Dynamic/RiserLine"]
    assert len(dynamic.containers) == 10


# -- merge -----------------------------------------------------------------


def test_merge_pairs_containers_by_name():
    left, right = Container("root"), Container("root")
    add_signal(graft(left, Container("shared")), array_signal("a"))
    add_signal(graft(right, Container("shared")), array_signal("b"))
    graft(right, Container("only-right"))

    merge_containers(left, right)

    assert [c.name for c in left.containers] == ["shared", "only-right"]
    assert [s.name for s in left["shared"].signals] == ["a", "b"]


def test_same_named_signals_are_both_kept():
    """Same-named siblings are legitimate, so the merge keeps both; renaming comes after."""
    left, right = Container("root"), Container("root")
    add_signal(left, constant("same", 1.0))
    add_signal(right, constant("same", 2.0))

    merge_containers(left, right)

    assert [(s.name, s.y[0]) for s in left.signals] == [("same", 1.0), ("same", 2.0)]


def test_merging_is_additive():
    """Two readers may describe one thing at different levels of detail.

    A RIFLEX MatrixPlot knows a line is a line; sima_elmfor.h5 only knows its
    name. Requiring identical attributes, as SIMA does, would leave the
    same line in the tree twice.
    """
    left, right = Container("root"), Container("root")
    graft(left, Container("MooringLine1", type="line"))
    graft(right, Container("MooringLine1", line="MooringLine1"))

    merge_containers(left, right)

    assert len(left.containers) == 1
    assert left["MooringLine1"].attributes == {"type": "line", "line": "MooringLine1"}


def test_a_merge_that_would_destroy_information_is_refused():
    """Same key, different values: they describe different things."""
    left, right = Container("root"), Container("root")
    graft(left, Container("x", type="static"))
    graft(right, Container("x", type="dynamic"))

    with pytest.warns(UserWarning, match="disagree on type"):
        merge_containers(left, right)

    assert len(left.containers) == 2
    assert [c.type for c in left.containers] == ["dynamic", "static"]
    assert [c.name for c in left.containers] == ["x", "x"]


def _item(name: str, type: str | None = None, index: str | None = None) -> Container:
    return Container(name, type, **({} if index is None else {"index": index}))


@pytest.mark.parametrize("items, expected", [
    ([("X", "b"), ("Y", "a"), ("Z",)], ["Y", "X", "Z"]),
    ([("zebra", "line"), ("apple",)], ["zebra", "apple"]),
    ([("s2", "segment", "2"), ("s1", "segment", "1"), ("line", "line")], ["line", "s1", "s2"]),
    ([("s3", "seg", "3"), ("s", "seg"), ("s1", "seg", "1")], ["s3", "s", "s1"]),
    ([("s3", "seg", "3"), ("s1", "seg", "1"), ("s", "seg")], ["s1", "s3", "s"]),
    ([("s", "seg"), ("s3", "seg", "3"), ("s1", "seg", "1")], ["s", "s1", "s3"]),
    ([("line", "line"), ("s2", "seg", "2"), ("u",), ("s1", "seg", "1"), ("body", "body")],
     ["line", "s2", "u", "body", "s1"]),
    ([("s10", "seg", "10"), ("s2", "seg", "2"), ("bad", "seg", "x"), ("s1", "seg", "1")],
     ["s1", "s2", "s10", "bad"]),
], ids=[
    "typed-before-untyped", "untyped-ties", "type-then-index", "unindexed-between",
    "unindexed-last", "unindexed-first", "untyped-in-the-middle", "unparseable-index",
])
def test_siblings_sort_as_simas_comparator_does(items, expected):
    """Each expected order is what java.util.List.sort gives with the comparator
    of SignalItemUtil.java:711-734. It is not a total order, so the input order
    shows through wherever it ties."""
    assert [c.name for c in merge_items([_item(*item) for item in items])] == expected


def test_shallow_copy_carries_identity_but_no_content():
    original = Container("Static", type="static")
    add_signal(original, array_signal("x"))

    clone = shallow_copy(original)

    assert (clone.name, clone.type) == ("Static", "static")
    assert len(clone) == 0


def test_prune_removes_empty_containers():
    root = Container("root")
    graft(root, Container("empty"))
    add_signal(graft(root, Container("full")), array_signal("x"))

    prune_empty(root)

    assert [c.name for c in root.containers] == ["full"]


# -- best effort -----------------------------------------------------------


def test_a_file_no_reader_claims_is_not_described(copy_run):
    """A run folder is mostly not results, and none of that is a gap in simapy.

    So a file nothing reads is left out rather than reported, which would say
    the opposite.
    """
    run = copy_run(RUN, extra={"vis.ldat": b"not read"})
    res = open_results(run)

    assert find_reader(run / "vis.ldat") is None
    assert [s.file for s in res.sources] == ["sima_stamod.mpf", "sima_dynmod.mpf"]


def test_a_file_that_vanishes_is_reported_not_fatal():
    """The folder is listed, then read, so a file can go between the two."""
    description = RunDescription(
        task="Simple_Flexible_Riser",
        condition="Initial",
        entries=(Entry(name="Static", results=(ResultFile("gone.mpf"),)),),
    )

    with pytest.warns(UserWarning, match="gone.mpf"):
        _, reports = build_tree(description, RUN)

    assert [r.status for r in reports] == [Status.MISSING]


def test_a_described_file_no_reader_claims_fails_in_place():
    """Unreachable from a scan, which lists only what a reader claims.

    Still reachable through build_tree: names.map is a real file in that folder
    and nothing reads .map, so it fails as any unreadable result does.
    """
    description = RunDescription(
        task="Simple_Flexible_Riser",
        condition="Initial",
        entries=(Entry(name="Static", results=(ResultFile("names.map"),)),),
    )

    with pytest.warns(UserWarning, match="names.map"):
        root, reports = build_tree(description, RUN)

    assert [r.status for r in reports] == [Status.FAILED]
    assert [type(n) for n in root.walk() if isinstance(n, Signal)] == [ErrorSignal]


def test_a_failing_reader_leaves_a_node_in_the_tree(copy_run):
    run = copy_run(RUN)
    (run / "sima_dynmod.mpf").write_text("MATRIX    truncated, line Risea63d\n")

    with pytest.warns(UserWarning, match="sima_dynmod.mpf"):
        res = open_results(run)

    failed = [s for s in res.sources if s.status is Status.FAILED]
    assert len(failed) == 1

    errors = [n for n in res.walk() if isinstance(n, ErrorSignal)]
    assert len(errors) == 1
    assert errors[0].path.startswith("Initial/Dynamic/")
    with pytest.raises(SourceError, match="Unable to import result"):
        _ = errors[0].y

    # The other file still imported.
    assert len(res["Initial/Static/RiserLine"].containers) == 7


def test_a_folder_with_no_result_file_is_an_error(tmp_path):
    with pytest.raises(ResultsError, match="holds no result files$"):
        open_results(tmp_path)


def test_a_folder_that_is_not_a_directory_is_an_error(tmp_path):
    with pytest.raises(ResultsError, match="not a directory"):
        open_results(tmp_path / "nope")


def test_a_flattened_entry_grafts_onto_the_condition():
    """What a file whose name says nothing about its analysis gets.

    Both files' RiserLine content then merges into one container, which is why
    the scan groups by analysis instead when it can.
    """
    description = RunDescription(
        task="Simple_Flexible_Riser",
        condition="Initial",
        entries=(
            Entry(
                name="",
                container=False,
                results=(ResultFile("sima_stamod.mpf"), ResultFile("sima_dynmod.mpf")),
            ),
        ),
        # So the assertion is about the graft and not about a hashed line id.
        names=scan.read_names(RUN),
    )

    condition = build_tree(description, RUN)[0]["Initial"]

    assert "Static" not in condition.keys()
    assert len(condition["RiserLine"].containers) == 17


def test_variable_values_become_a_container(copy_run, variables_inp):
    run = copy_run(
        RUN,
        extra={
            "variables.inp": variables_inp(
                "Simple_Flexible_Riser", doubleVariables={"Hs": 3.0, "Tp": 10.0}
            )
        },
    )

    variables = open_results(run)["Initial/Variables"]

    assert variables.keys() == ["Hs", "Tp"]
    assert variables["Hs"].y[0] == 3.0
    assert variables["Hs"].type == "variable"
    # The unit is in the model, not on disk, so it defaults as SIMA defaults it.
    assert variables["Hs"].unit == "-"
    # And the container is inserted first, ahead of the results.
    assert open_results(run)["Initial"].keys()[0] == "Variables"

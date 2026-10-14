"""Working out what a run folder holds, from the folder.

One folder is one run. What is under test here is the derivation -- which files
count as results, which analysis each belongs to, and the little that names the
run -- not the reading, which the reader tests cover.

That the derivation is *right* is settled elsewhere and more strongly:
``test_results_oracle.py`` compares the tree these fixtures produce against
``Riflex_Results.h5``, which SIMA's own post processor wrote from the same run.
"""

import json
import shutil
import warnings
from pathlib import Path

import pytest

from simapy_results import (ResultsError, Status, UnsupportedStorageWarning, Variable,
                            open_results)
from simapy_results import _scan as scan
from simapy_results._scan import find_runs, holds_results

from .conftest import DATA

RIFLEX = DATA / "Simple_Flexible_Riser" / "Initial"


def _touch(folder: Path, *names: str) -> Path:
    """Empty placeholders. What is under test is the derivation, not reading."""
    folder.mkdir(parents=True, exist_ok=True)
    for name in names:
        (folder / name).write_bytes(b"")
    return folder


def _described_files(folder: Path) -> set[str]:
    return {r.file for e in scan.describe(folder).entries for r in e.results}


# -- what names the run -----------------------------------------------------


def test_the_task_and_condition_come_from_the_folder_path(tmp_path):
    folder = _touch(tmp_path / "Heavy_Lifting_Operation" / "Initial", "ts_buffer.b5")

    described = scan.describe(folder)

    assert (described.task, described.condition) == (
        "Heavy_Lifting_Operation",
        "Initial",
    )


def test_a_timestamp_folder_reports_the_condition_it_belongs_to(tmp_path):
    """Otherwise every path would be prefixed ``1-20260901063413``.

    The name's format is fixed by SIMA, so skipping it
    is naming and not discovery -- no folder is chosen over another.
    """
    folder = _touch(
        tmp_path / "Heavy_Lifting_Operation" / "Initial" / "1-20260901063413",
        "ts_buffer.b5",
    )

    described = scan.describe(folder)

    assert (described.task, described.condition) == (
        "Heavy_Lifting_Operation",
        "Initial",
    )


def test_the_variables_file_names_the_task_better_than_the_path_can(
    tmp_path, variables_inp
):
    """A set member's folders sit under the set, not under the task.

    So the path alone reports ``ConditionSet`` as the task. The header of
    ``variables.inp`` names the real one, and it is in the folder already.
    """
    folder = _touch(
        tmp_path / "ConditionSet" / "1-20260901083940" / "ConditionSet_1",
        "ts_buffer.b5",
    )
    assert scan.describe(folder).task == "ConditionSet"  # what the path implies

    (folder / "variables.inp").write_bytes(
        variables_inp("Heavy_Lifting_Operation", doubleVariables={"hs": 1.5})
    )

    described = scan.describe(folder)
    assert (described.task, described.condition) == (
        "Heavy_Lifting_Operation",
        "ConditionSet_1",
    )


def test_a_flat_work_directory_is_named_after_itself(tmp_path):
    """The shape a solver harness produces, with no SIMA layout around it."""
    folder = _touch(tmp_path / "S101_FPSO" / "work", "sima_dynmod.mpf")

    described = scan.describe(folder)

    assert (described.task, described.condition) == ("S101_FPSO", "work")


# -- variable values --------------------------------------------------------


def test_variable_values_are_read_from_the_folder(tmp_path, variables_inp):
    """The one thing only the model knew that a folder still holds.

    A set member's folder carries the values that member ran with, which is why
    nothing outside the folder has to describe them.
    """
    folder = _touch(tmp_path / "Task" / "ConditionSpace_1")
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": 1.1, "tp": 10.0})
    )

    variables = scan.describe(folder).variables

    assert {n: v.value for n, v in variables.items()} == {"hs": 1.1, "tp": 10.0}


def test_the_declaring_reference_types_each_value(tmp_path, variables_inp):
    """``getValueAsString`` writes text; the block header says what it was.

    Without that an integer variable would come back as a float.
    """
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "variables.inp").write_bytes(
        variables_inp(
            "Task",
            doubleVariables={"hs": 1.5},
            integerVariables={"seed": 3},
            stringVariables={"label": "north"},
        )
    )

    values = {n: v.value for n, v in scan.describe(folder).variables.items()}

    assert values == {"hs": 1.5, "seed": 3, "label": "north"}
    assert [type(v) for v in values.values()] == [float, int, str]


def test_a_variable_carries_no_unit_without_a_manifest(tmp_path, variables_inp):
    """``variables.inp`` holds values only, so the tree stamps ``-`` as SIMA does."""
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": 1.5})
    )

    assert scan.describe(folder).variables["hs"].unit is None


# -- variables from results.json; variables.inp only without one -----------

#: One condition set as SIMA writes it (sima/sima/sima-platform#59):
#: BouncingBalls/conditionSet, members varying ``kzz``.
SET_MANIFEST = {
    "task": "BouncingBalls",
    "condition": "conditionSet",
    "conditions": [
        {"condition": "conditionSet_1", "variables": {"kzz": {"value": 500.0, "unit": "N*m"}}},
        {"condition": "conditionSet_2", "variables": {"kzz": {"value": 5000.0, "unit": "N*m"}}},
    ],
}


def _manifest(condition: Path, content: dict) -> None:
    condition.mkdir(parents=True, exist_ok=True)
    (condition / scan.RESULTS_FILENAME).write_text(
        json.dumps(content), encoding="utf-8"
    )


def test_a_manifest_gives_values_and_units(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition" / "1-20260919071348")
    _manifest(folder.parent, {"task": "Task", "condition": "Condition",
                              "variables": {"hs": {"value": 1.5, "unit": "m"},
                                         "seed": {"value": 3}}})

    variables = scan.describe(folder).variables
    assert (variables["hs"].value, variables["hs"].unit) == (1.5, "m")
    assert str(variables["hs"]) == "1.5 [m]"
    assert (variables["seed"].value, variables["seed"].unit) == (3, None)
    assert isinstance(variables["seed"].value, int)


def test_a_set_member_takes_its_own_variables(tmp_path):
    """The manifest sits at the condition, two levels up, and describes every member."""
    condition = tmp_path / "BouncingBalls" / "conditionSet"
    run = condition / "1-20260919071348"
    for name in ("conditionSet_1", "conditionSet_2"):
        _touch(run / name)
    _manifest(condition, SET_MANIFEST)

    assert scan.read_manifest_variables(run / "conditionSet_1") == {"kzz": Variable(500.0, "N*m")}
    assert scan.describe(run / "conditionSet_2").variables["kzz"] == Variable(5000.0, "N*m")


def test_a_member_block_wins_over_the_sets_constants(tmp_path):
    """A set records what it holds constant at the top and each member's own below."""
    condition = tmp_path / "Task" / "Set"
    member = _touch(condition / "1-20260919071348" / "Set_1")
    _manifest(condition, {
        "task": "Task", "condition": "Set",
        "variables": {"hs": {"value": 0.0, "unit": "foot"},
                   "depth": {"value": 100.0, "unit": "m"}},
        "conditions": [{"condition": "Set_1",
                        "variables": {"hs": {"value": 1.5, "unit": "m"}}}],
    })

    assert scan.read_manifest_variables(member) == {
        "hs": Variable(1.5, "m"), "depth": Variable(100.0, "m")}


def test_a_manifest_with_values_is_the_only_source(tmp_path, variables_inp):
    """Values and units come from one place; variables.inp is not consulted."""
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": 9.0, "tp": 10.0})
    )
    _manifest(folder, {"task": "Task", "condition": "Condition",
                       "variables": {"hs": {"value": 1.5, "unit": "m"}}})

    assert scan.describe(folder).variables == {"hs": Variable(1.5, "m")}


def test_a_manifest_without_values_leaves_the_variables_file(tmp_path, variables_inp):
    """As run_condition's own naming file, or a condition with no variables."""
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": 1.5})
    )
    _manifest(folder, {"task": "Task", "condition": "Condition"})

    assert scan.read_manifest_variables(folder) is None
    assert scan.describe(folder).variables == {"hs": Variable(1.5)}


def test_a_member_the_set_does_not_list_reads_its_variables_file(tmp_path, variables_inp):
    """The set's constants alone would be a wrong answer for a member it does not know."""
    condition = tmp_path / "BouncingBalls" / "conditionSet"
    member = _touch(condition / "1-20260919071348" / "conditionSet_9")
    (member / "variables.inp").write_bytes(
        variables_inp("BouncingBalls", doubleVariables={"kzz": 900.0})
    )
    _manifest(condition, SET_MANIFEST)

    assert scan.describe(member).variables == {"kzz": Variable(900.0)}


def test_an_unreadable_manifest_reads_the_variables_file(tmp_path, variables_inp):
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": 1.5})
    )
    (folder / scan.RESULTS_FILENAME).write_text("{ truncated", encoding="utf-8")

    description = scan.describe(folder)
    assert description.variables == {"hs": Variable(1.5)}
    assert description.condition == "Condition", "still named from the folder"


def test_the_unit_reaches_the_tree(tmp_path, variables_inp):
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "sima_stamod.mpf").write_bytes(
        (RIFLEX / "sima_stamod.mpf").read_bytes()
    )
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": 1.5})
    )
    _manifest(folder, {"task": "Task", "condition": "Condition",
                       "variables": {"hs": {"value": 1.5, "unit": "m"}}})

    assert open_results(folder)["Condition/Variables/hs"].unit == "m"


def test_a_value_that_will_not_parse_keeps_its_text(tmp_path, variables_inp):
    """The value the run used matters more than the type it was declared with."""
    folder = _touch(tmp_path / "Task" / "Condition")
    (folder / "variables.inp").write_bytes(
        variables_inp("Task", doubleVariables={"hs": "not a number"})
    )

    assert scan.describe(folder).variables["hs"].value == "not a number"


def test_no_variables_file_is_not_an_error(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition", "ts_buffer.b5")

    described = scan.describe(folder)

    assert described.variables == {}
    assert described.task == "Task"


# -- curation ---------------------------------------------------------------


@pytest.mark.parametrize("identifier", ["", "-sima"], ids=["simo", "coupled"])
def test_internal_h5_files_are_excluded_but_the_two_result_ones_are_not(
    identifier, tmp_path
):
    """``isSimoInternalFile`` names six files; two of them are results anyway.

    The factories add those two back explicitly and the predicate only stops the
    ``*.h5`` glob adding them twice. Missing either loses a whole analysis, so
    both spellings of both names are pinned here.
    """
    folder = _touch(
        tmp_path / "Task" / "Condition",
        f"simo{identifier}.h5",
        f"simo-intermediate{identifier}.h5",
        f"simstab-intermediate{identifier}.h5",
        "env.h5",
        f"simo-static-results{identifier}.h5",
        f"simo-dynamic-results{identifier}.h5",
    )

    assert _described_files(folder) == {
        f"simo-static-results{identifier}.h5",
        f"simo-dynamic-results{identifier}.h5",
    }


def test_internal_files_are_excluded_whatever_their_case(tmp_path):
    """Java compares case sensitively; the file systems these live on do not."""
    folder = _touch(tmp_path / "Task" / "Condition", "ENV.H5", "Simo-Intermediate.h5")

    assert _described_files(folder) == set()


def test_the_files_read_for_context_are_not_also_results(tmp_path):
    """And a stray results.json is not one either, whoever wrote it."""
    folder = _touch(
        tmp_path / "Task" / "Condition", "names.map", "variables.inp", "results.json"
    )

    assert _described_files(folder) == set()


def test_solver_input_is_not_described(tmp_path):
    """A run folder is mostly input, and none of it is a gap in simapy, so files
    no reader claims are left out of the description entirely."""
    folder = _touch(
        tmp_path / "Task" / "Condition",
        "SIMO_DEF.DAT",
        "sys.dat",
        "stamod.inp",
        "simo_dynmod_input.inp",
        "simores.inp",
        "ini.sam",
        "dynmod_stdout13100344102566801413.txt",
        "ts_buffer.b5",
    )

    assert _described_files(folder) == {"ts_buffer.b5"}

    # The placeholder is empty, so reading it fails -- but it was the only file
    # offered, which is what this pins.
    with pytest.warns(UserWarning, match="ts_buffer.b5"):
        res = open_results(folder)
    assert [s.file for s in res.sources] == ["ts_buffer.b5"]


# -- storage formats simapy does not read ------------------------------------


def _old_storage(folder: Path) -> Path:
    """A RIFLEX run with binary and ASCII storage, and a SIMO one with the old result structure."""
    _riflex_run(folder, "sima_stamod.mpf", "sima_dynmod.mpf")
    return _touch(folder, "sima_noddis.bin", "key_sima_noddis.txt", "sima_elmfor.bin",
                  "key_sima_elmfor.txt", "sima_elmcur.asc", "key_sima_elmcur.txt",
                  "results.tda", "results.txt")


def test_old_storage_is_reported_and_the_rest_still_read(tmp_path):
    folder = _old_storage(tmp_path / "Simple_Flexible_Riser" / "Initial")

    with pytest.warns(UnsupportedStorageWarning, match="cannot read 4 result files") as caught:
        res = open_results(folder)

    assert {s.file: s.status for s in res.sources} == {
        "sima_stamod.mpf": Status.READ,
        "sima_dynmod.mpf": Status.READ,
        "results.tda": Status.UNSUPPORTED,
        "sima_elmcur.asc": Status.UNSUPPORTED,
        "sima_elmfor.bin": Status.UNSUPPORTED,
        "sima_noddis.bin": Status.UNSUPPORTED,
    }
    assert res.run["Dynamic/RiserLine"]
    message = str(caught[0].message)
    assert '  sima_elmfor.bin, sima_noddis.bin: RIFLEX binary storage. In SIMA, set the RIFLEX ' \
           'storage format to "Default" (HDF5), and run again.' in message
    assert "sima_elmcur.asc: RIFLEX ASCII storage" in message
    assert 'results.tda: SIMO\'s old result structure. In SIMA, clear "Use old result structure"' in message


def test_an_asc_file_without_a_key_file_is_not_storage(tmp_path):
    """RIFLEX writes other .asc files, such as the static configuration; only storage has a key file."""
    folder = _riflex_run(tmp_path / "Task" / "Condition", "sima_stamod.mpf")
    _touch(folder, "sima_consta.asc", "sima_massin.asc", "sima.bin")

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        res = open_results(folder)

    assert [s.file for s in res.sources] == ["sima_stamod.mpf"]


def test_a_folder_of_old_storage_alone_says_how_to_fix_it(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition", "sima_noddis.bin", "key_sima_noddis.txt")

    with pytest.raises(ResultsError, match=r'only results simapy cannot read:\n  sima_noddis.bin: .*"Default"'):
        open_results(folder)


def test_opening_an_old_storage_file_says_how_to_fix_it(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition", "results.tda")

    with pytest.raises(ResultsError, match="cannot read results.tda: .*Use old result structure"):
        open_results(folder / "results.tda")


def test_a_condition_reports_old_storage_in_its_run_folders(tmp_path):
    condition = tmp_path / "Simple_Flexible_Riser" / "Initial"
    _old_storage(condition / "1-20261002061613")
    _manifest(condition, {"task": "Simple_Flexible_Riser", "condition": "Initial",
                          "directories": {"Static": "1-20261002061613",
                                          "Dynamic": "1-20261002061613"}})

    with pytest.warns(UnsupportedStorageWarning, match="1-20261002061613/sima_noddis.bin"):
        res = open_results(condition)

    assert [s.file for s in res.sources if s.status is Status.UNSUPPORTED] == [
        "1-20261002061613/results.tda", "1-20261002061613/sima_elmcur.asc",
        "1-20261002061613/sima_elmfor.bin", "1-20261002061613/sima_noddis.bin"]


# -- grouping by analysis ---------------------------------------------------


def test_static_and_dynamic_in_one_folder_go_to_separate_entries(tmp_path):
    """A layout SIMA really produces, for a run that did both."""
    folder = _touch(
        tmp_path / "Task" / "Initial",
        "simo-static-results.h5",
        "simo-dynamic-results.h5",
        "ts_buffer.b5",
        # Real results SIMA registers, but no reader here claims them.
        "prs.lis",
        "prd.lis",
    )

    entries = {
        e.name: (e.run_type, sorted(r.file for r in e.results))
        for e in scan.describe(folder).entries
    }
    assert entries == {
        "Static": ("static", ["simo-static-results.h5"]),
        "Dynamic": ("dynamic", ["simo-dynamic-results.h5", "ts_buffer.b5"]),
    }


def test_the_fixture_folder_groups_its_two_mpf_files_by_module():
    described = scan.describe(RIFLEX)

    assert [(e.name, e.run_type) for e in described.entries] == [
        ("Static", "static"),
        ("Dynamic", "dynamic"),
    ]


def test_static_and_dynamic_mpf_do_not_merge_their_lines():
    """Both files hold a ``RiserLine`` container, and merging fuses by name.

    So without grouping by analysis a static result would land inside a dynamic
    one. This is why the grouping exists at all.
    """
    res = open_results(RIFLEX)

    static = res.container("Initial/Static/RiserLine")
    dynamic = res.container("Initial/Dynamic/RiserLine")
    assert [c.name for c in static.containers]
    assert [c.name for c in dynamic.containers]
    assert not {c.name for c in static.containers} & {c.name for c in dynamic.containers}


def test_a_file_that_names_no_analysis_is_grafted_onto_the_condition(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition", "gzCurve.h5", "sima_stamod.mpf")

    entries = {e.name: e.container for e in scan.describe(folder).entries}

    assert entries == {"Static": True, "": False}


def test_entries_come_out_in_analysis_order_not_file_order(tmp_path):
    """Entry order is child order in the tree, so it must not follow the sort."""
    folder = _touch(
        tmp_path / "Task" / "Condition",
        "sima_dynmod.mpf",
        "sima_eigmod.mpf",
        "sima_stamod.mpf",
    )

    assert [e.name for e in scan.describe(folder).entries] == [
        "Static",
        "Dynamic",
        "Eigenvalue",
    ]


# -- one folder, one run ----------------------------------------------------


def test_a_folder_of_timestamp_subfolders_names_them_instead_of_choosing(tmp_path):
    """Nothing on disk says which of them is current, so none is chosen.

    Both of these are run 1 -- ``runNumber`` does not separate them and mtime is
    a guess -- so the caller says which run it means.
    """
    folder = tmp_path / "Task" / "Condition"
    _touch(folder / "1-20260901083636", "simo-static-results.h5")
    _touch(folder / "1-20260901083822", "simo-dynamic-results.h5")

    assert scan.describe(folder).entries == ()
    with pytest.raises(ResultsError, match="1-20260901083636, 1-20260901083822$"):
        open_results(folder)


def test_analyses_in_separate_folders_are_separate_runs(tmp_path):
    """The ConditionSpace layout: static and dynamic under different timestamps.

    Each folder describes itself, so one call gives one analysis. Combining them
    is the caller's to do, because only the caller knows they belong together.
    """
    condition = tmp_path / "Task" / "Condition"
    static = _touch(condition / "1-20260901083636", "sima_stamod.mpf")
    dynamic = _touch(condition / "1-20260901083822", "sima_dynmod.mpf")

    assert [e.name for e in scan.describe(static).entries] == ["Static"]
    assert [e.name for e in scan.describe(dynamic).entries] == ["Dynamic"]
    assert scan.describe(static).condition == scan.describe(dynamic).condition


def test_find_runs_lists_each_working_directory(tmp_path):
    condition = tmp_path / "Task" / "Condition"
    static = _touch(condition / "1-20260901083636", "sima_stamod.mpf")
    dynamic = _touch(condition / "1-20260901083822", "sima_dynmod.mpf")
    _touch(condition / "not-a-run", "sima_stamod.mpf")

    assert find_runs(condition) == [static, dynamic]


def test_find_runs_lists_the_members_of_a_set(tmp_path):
    condition = tmp_path / "Task" / "Set"
    run = condition / "1-20260901083940"
    members = [_touch(run / f"Set_{n}", "sima_dynmod.mpf") for n in (1, 2)]

    assert find_runs(condition) == members


def test_a_condition_holding_results_itself_is_its_own_run(tmp_path):
    """The flat layout, with results directly in the condition folder."""
    condition = _touch(tmp_path / "Task" / "Condition", "sima_stamod.mpf")
    run = _touch(condition / "1-20260901083636", "sima_dynmod.mpf")

    assert holds_results(condition)
    assert find_runs(condition) == [condition, run]


def test_working_files_alone_are_not_results(tmp_path):
    """A run that left only solver working files has nothing to open."""
    condition = tmp_path / "Task" / "Condition"
    run = _touch(condition / "1-20260901083636", "simo.h5", "env.h5")

    assert not holds_results(run)
    assert find_runs(condition) == []


def test_a_missing_folder_holds_no_results(tmp_path):
    assert not holds_results(tmp_path / "nope")
    assert find_runs(tmp_path / "nope") == []


# -- names.map --------------------------------------------------------------


def test_the_id_map_is_read_as_alternating_lines(tmp_path):
    folder = tmp_path / "Task" / "Condition"
    folder.mkdir(parents=True)
    (folder / "names.map").write_bytes(
        b"Risea63d\r\nRiserLine\r\nBalld9ab\r\nBallJoint\r\n"
    )

    assert scan.read_names(folder) == {
        "Risea63d": "RiserLine",
        "Balld9ab": "BallJoint",
    }
    assert scan.describe(folder).names == scan.read_names(folder)


def test_a_missing_id_map_is_not_an_error(tmp_path):
    folder = tmp_path / "Task" / "Condition"
    folder.mkdir(parents=True)

    assert scan.read_names(folder) == {}


def test_an_odd_id_map_yields_no_names_rather_than_half_a_map(tmp_path):
    """Hashed line ids are a cosmetic loss; a half-applied map is a wrong one."""
    folder = tmp_path / "Task" / "Condition"
    folder.mkdir(parents=True)
    (folder / "names.map").write_bytes(b"Risea63d\nRiserLine\nOrphan\n")

    assert scan.read_names(folder) == {}


def test_the_id_map_resolves_the_names_in_the_tree(copy_run):
    """Its one visible effect, and what a missing one costs."""
    assert "Initial/Static/RiserLine" in open_results(RIFLEX)

    run = copy_run(RIFLEX)
    (run / "names.map").unlink()

    res = open_results(run)
    assert "Initial/Static/RiserLine" not in res
    assert any("Risea63d" in path for path in res.select())


def test_a_caller_can_supply_names_the_folder_lacks(copy_run):
    """RIFLEX writes names.map only in the dynmod folder.

    So a static-only run cannot resolve its own line ids. The map is
    task-level, which is what makes a sibling run's copy the right answer --
    but only a caller knows the two runs belong together.
    """
    run = copy_run(RIFLEX)
    borrowed = scan.read_names(run)
    (run / "names.map").unlink()

    assert "Initial/Static/RiserLine" not in open_results(run)
    assert "Initial/Static/RiserLine" in open_results(run, names=borrowed)


def test_supplied_names_win_over_the_folders_own(copy_run):
    run = copy_run(RIFLEX)

    described = scan.describe(run, names={"Risea63d": "Borrowed"})

    assert described.names["Risea63d"] == "Borrowed"
    # And the rest of the folder's own map is still there.
    assert len(described.names) == len(scan.read_names(run))


# -- a condition opened from its results.json ------------------------------


def _riflex_run(folder: Path, *files: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for name in files:
        (folder / name).write_bytes((RIFLEX / name).read_bytes())
    (folder / "names.map").write_bytes((RIFLEX / "names.map").read_bytes())
    return folder


def test_analyses_run_apart_become_one_tree(tmp_path):
    condition = tmp_path / "Simple_Flexible_Riser" / "Initial"
    _riflex_run(condition / "1-20261002061606", "sima_stamod.mpf")
    _riflex_run(condition / "1-20261002061613", "sima_dynmod.mpf")
    _manifest(condition, {"task": "Simple_Flexible_Riser", "condition": "Initial",
                          "variables": {"hs": {"value": 1.5, "unit": "m"}},
                          "directories": {"Static": "1-20261002061606",
                                          "Dynamic": "1-20261002061613"}})

    res = open_results(condition)

    assert [c.name for c in res.run.containers] == ["Variables", "Static", "Dynamic"]
    assert [s.file for s in res.sources] == ["1-20261002061606/sima_stamod.mpf",
                                             "1-20261002061613/sima_dynmod.mpf"]
    assert res.run["Static/RiserLine/Static forces/EFF. TENSION"].unit == "N"
    assert res.run["Variables/hs"].unit == "m"


def test_a_folder_gives_only_the_analysis_it_is_named_for(tmp_path):
    """SIMA copies static results into the dynamic folder; that copy is not this run's."""
    condition = tmp_path / "Simple_Flexible_Riser" / "Initial"
    _riflex_run(condition / "1-static", "sima_stamod.mpf")
    _riflex_run(condition / "1-dynamic", "sima_dynmod.mpf", "sima_stamod.mpf")
    _manifest(condition, {"task": "Simple_Flexible_Riser", "condition": "Initial",
                          "directories": {"Static": "1-static", "Dynamic": "1-dynamic"}})

    assert [s.file for s in open_results(condition).sources] == [
        "1-static/sima_stamod.mpf", "1-dynamic/sima_dynmod.mpf"]


def test_a_stale_folder_is_never_read(tmp_path):
    condition = tmp_path / "Simple_Flexible_Riser" / "Initial"
    _riflex_run(condition / "1-20260101000000", "sima_stamod.mpf", "sima_dynmod.mpf")
    _riflex_run(condition / "2-20261002061602", "sima_stamod.mpf", "sima_dynmod.mpf")
    _manifest(condition, {"task": "Simple_Flexible_Riser", "condition": "Initial",
                          "directories": {"Static": "2-20261002061602",
                                          "Dynamic": "2-20261002061602"}})

    assert {Path(s.file).parent.name for s in open_results(condition).sources} == {"2-20261002061602"}


def test_results_in_the_condition_root_are_named_by_a_dot(tmp_path):
    condition = _riflex_run(tmp_path / "Simple_Flexible_Riser" / "Initial", "sima_stamod.mpf")
    _manifest(condition, {"task": "Simple_Flexible_Riser", "condition": "Initial",
                          "directories": {"Static": "."}})

    assert [s.file for s in open_results(condition).sources] == ["sima_stamod.mpf"]


def test_without_directories_the_condition_folder_is_not_a_run(tmp_path):
    condition = tmp_path / "Task" / "Condition"
    _touch(condition / "1-20261002061606", "ts_buffer.b5")
    _manifest(condition, {"task": "Task", "condition": "Condition"})

    assert scan.describe_condition(condition) is None
    with pytest.raises(ResultsError, match="1-20261002061606"):
        open_results(condition)


def test_a_condition_names_itself_as_its_condition_container(tmp_path):
    condition = _riflex_run(tmp_path / "Simple_Flexible_Riser" / "Initial", "sima_stamod.mpf")

    assert open_results(condition).run.attributes["conditionContainer"] == "Initial"


def test_a_set_reads_as_task_set_and_members(tmp_path):
    """The tree SIMA's post processor shows for a set, static and dynamic paired per member."""
    condition = tmp_path / "Simple_Flexible_Riser" / "ConditionSet1"
    for member in ("ConditionSet1_1", "ConditionSet1_2"):
        _riflex_run(condition / "1-20261002061934" / member, "sima_stamod.mpf")
        _riflex_run(condition / "1-20261002061938" / member, "sima_dynmod.mpf")
    _manifest(condition, {
        "task": "Simple_Flexible_Riser", "condition": "ConditionSet1",
        "variables": {"depth": {"value": 100.0, "unit": "m"}},
        "conditions": [
            {"condition": member,
             "variables": {"direction": {"value": float(index * 10), "unit": "deg"}},
             "directories": {"Static": f"1-20261002061934/{member}",
                             "Dynamic": f"1-20261002061938/{member}"}}
            for index, member in enumerate(("ConditionSet1_1", "ConditionSet1_2"))
        ],
    })

    res = open_results(condition)

    assert res.type == "task"
    assert (res.run.name, res.run.type) == ("ConditionSet1", "conditionContainer")
    assert [c.name for c in res.run.containers] == ["Variables", "ConditionSet1_1", "ConditionSet1_2"]
    member = res.run.container("ConditionSet1_2")
    assert member.type == "condition"
    assert member.attributes["conditionContainer"] == "ConditionSet1"
    assert [c.name for c in member.containers] == ["Variables", "Static", "Dynamic"]
    assert member["Variables/direction"].y[0] == 10.0
    assert res.run["Variables/depth"].unit == "m"
    assert [m.condition for m in res.description.members] == ["ConditionSet1_1", "ConditionSet1_2"]
    assert len(res.sources) == 4


def test_a_set_member_without_directories_leaves_the_set_unread(tmp_path):
    condition = tmp_path / "Task" / "Set"
    _touch(condition / "1-20261002061934" / "Set_1", "ts_buffer.b5")
    _manifest(condition, {"task": "Task", "condition": "Set",
                          "conditions": [{"condition": "Set_1"}]})

    assert scan.describe_condition(condition) is None


def test_outmod_results_belong_to_the_dynamic_analysis():
    """SIMA holds them in the dynamic entry, so they land under Dynamic."""
    assert scan.phase_of("sima_outmod.mpf") == ("Dynamic", "dynamic")


# -- riflexres.inp, where SIMA's MPF import takes its line names ------------


def test_riflexres_names_every_line_and_id():
    """A static run on its own, as RIFLEX left it: riflexres.inp and no names.map."""
    names = scan.read_names(DATA / "riflexres")

    assert names["well18c5"] == "well_line"
    assert names["slip0e68"] == "slipjoint_above"
    assert [names[f"tens{suffix}"] for suffix in ("cc81", "a520", "7dbf", "565e", "2efd", "079c")] == [
        f"tensioner{n}_line" for n in range(1, 7)]
    assert len(names) == 11


def test_riflexres_wins_over_names_map(tmp_path):
    shutil.copy(DATA / "riflexres" / "riflexres.inp", tmp_path / "riflexres.inp")
    (tmp_path / "names.map").write_bytes(b"slip0e68\r\nStale\r\nonly1234\r\nKept\r\n")

    names = scan.read_names(tmp_path)

    assert (names["slip0e68"], names["only1234"]) == ("slipjoint_above", "Kept")


def test_a_static_run_without_names_map_reads_its_lines_by_name(tmp_path):
    run = tmp_path / "Simple_Flexible_Riser" / "Initial"
    run.mkdir(parents=True)
    shutil.copy(RIFLEX / "sima_stamod.mpf", run / "sima_stamod.mpf")
    (run / "riflexres.inp").write_text(
        "'Version\n2.0.0\n'Number of line name mappings\n1\nRisea63d=RiserLine\n"
        "0\n0\n0\n", encoding="utf-8")

    assert "RiserLine" in open_results(run).run.container("Static")


def test_an_unreadable_riflexres_adds_no_names(tmp_path):
    (tmp_path / "riflexres.inp").write_text("'Version\n2.6.0\n'Lines\n3\nabc=def\n", encoding="utf-8")

    assert scan.read_names(tmp_path) == {}


def test_a_set_member_keeps_its_own_name(tmp_path):
    """results.json names the condition; a member is named by its folder."""
    condition = tmp_path / "Task" / "conditionSet"
    member = _riflex_run(condition / "1-20260901083937" / "conditionSet_2", "sima_stamod.mpf")
    (condition / "results.json").write_text(
        json.dumps({"task": "Task", "condition": "conditionSet"}), encoding="utf-8")

    res = open_results(member)
    assert res.description.condition == "conditionSet_2"
    assert res.description.task == "Task"


class TestHoldsResults:
    """Whether a folder holds anything a reader claims."""

    def test_a_result_file_counts(self, tmp_path):
        (tmp_path / "sima_dynmod.mpf").write_bytes(b"")
        assert holds_results(tmp_path)

    def test_solver_input_does_not(self, tmp_path):
        for name in ("stamod.inp", "sys.dat", "SIMO_DEF.DAT"):
            (tmp_path / name).write_bytes(b"")
        assert not holds_results(tmp_path)

    def test_nor_do_the_files_that_describe_the_run(self, tmp_path):
        """names.map and variables.inp travel with results but are not results."""
        for name in ("names.map", "variables.inp"):
            (tmp_path / name).write_bytes(b"")
        assert not holds_results(tmp_path)


def test_describe_overrides_reach_the_tree(tmp_path):
    """open_results names a run the folder cannot name itself."""
    folder = tmp_path / "copied"
    folder.mkdir()
    (folder / "sima_stamod.mpf").write_bytes(RIFLEX.joinpath("sima_stamod.mpf").read_bytes())

    default = open_results(folder)
    named = open_results(folder, task="Task", condition="Initial")
    assert default.description.condition == "copied"
    assert named.description.condition == "Initial"

"""SIMO static results as text: ``psc.lis``, named by ``simores.inp``.

The acceptance test is ``psc_oracle.json``: the tree SIMA itself built from the
``Heavy_Lifting_Operation`` static run whose files are in the data folder. The
rest transcribes SIMA's own tests and pins which ``psc.lis`` a scan offers.

SIMA's tests name their elements from a model. Here that model is replaced by a
hand-written ``simores.inp`` beside each copied ``psc.lis``, with the element
counts and the initial positions those tests rely on.
"""

import json
import shutil
from pathlib import Path

import pytest

from simapy.results import Container, ErrorSignal, ResultsError, Signal, Status, open_results
from simapy.results._scan import holds_results
from simapy.results import _scan as scan
from simapy.results._readers.psc import PscReader
from simapy.results._registry import find_reader
from simapy.results._sources import FolderContext, Source, SourceError

from .conftest import DATA
from .test_results_simos_r0 import _equally_spaced, _string

RUN = DATA / "Heavy_Lifting_Operation" / "Static"
ORACLE = DATA / "psc_oracle.json"
SYS_FRAM = DATA / "psc" / "sys-fram"
PARSER = DATA / "psc" / "parser"

#: From simo-static-results.h5, so not in the oracle.
CATENARY = "Catenary lines"

FACTOR = 1000.0


def _static(path: Path) -> Container:
    return open_results(path).run.container("Static")


def _value(signal: Signal) -> float:
    return float(signal.y[0])


def _tree(static: Container) -> dict:
    """The oracle's shape: body to container to ``[signal, unit, value]``."""
    return {
        body.name: {
            child.name: [[s.name, s.unit, _value(s)] for s in child.signals]
            for child in body.containers if child.name != CATENARY
        }
        for body in static.containers
    }


def _assert_matches_oracle(static: Container) -> None:
    expected = json.loads(ORACLE.read_text(encoding="utf-8"))["bodies"]
    got = _tree(static)

    assert list(got) == list(expected)
    for body, containers in expected.items():
        assert list(got[body]) == list(containers), body
        for name, signals in containers.items():
            found = got[body][name]
            assert [s[:2] for s in found] == [s[:2] for s in signals], (body, name)
            assert [s[2] for s in found] == pytest.approx([s[2] for s in signals], rel=1e-9), (body, name)

    for body in static.containers:
        assert (body.type, body.attributes["body"]) == ("body", body.name)
        for child in body.containers:
            if child.name == CATENARY:
                continue
            for signal in child.signals:
                assert (signal.xunit, signal.attributes["body"]) == ("-", body.name)


# -- the oracle -------------------------------------------------------------


def test_the_run_reproduces_the_tree_sima_built_from_it():
    _assert_matches_oracle(_static(RUN / "psc.lis"))


def test_beside_simo_static_results_each_body_gets_both(copy_run):
    """Both readers make a body container by name, and the merge joins them.

    The HDF5 is read first, as SIMOStaticResultFactory registers it, so SIMA's
    catenary lines lead each body.
    """
    run = copy_run(RUN)
    _static_results_h5(run / "simo-static-results.h5")

    res = open_results(run)
    static = res.run.container("Static")

    assert [(s.file, s.status) for s in res.sources] == [
        ("simo-static-results.h5", Status.READ), ("psc.lis", Status.READ)]
    platform = static.container("Platform")
    assert platform.container(CATENARY).signal("XBRLF force").unit == "N"
    assert [c.name for c in platform.containers][0] == CATENARY
    _assert_matches_oracle(static)


def _static_results_h5(path: Path) -> None:
    h5py = pytest.importorskip("h5py")
    with h5py.File(path, "w") as handle:
        handle.attrs["format"] = b"simos_r0"
        handle.attrs["order"] = b"results"
        _equally_spaced(handle, path="/results/bodies/0/catenary/force")
        _string(handle, "/results/bodies/0/catenary", "name", CATENARY)
        _string(handle, "/results/bodies/0", "name", "Platform")
        _string(handle, "/results/bodies", "name", "Bodies")


# -- SIMA's PSCMetaDataImporterTest ----------------------------------------


def test_psc_importer():
    """PSCMetaDataImporterTest.testPSCImporter, on sys-fram-psc.lis."""
    static = _static(SYS_FRAM / "psc.lis")
    assert len(static.containers) == 5

    trollc = static.containers[0]
    assert trollc.attributes["body"] == "TROLLC"
    children = trollc.containers
    assert len(children) == 45

    _assert_position(children[0], "Initial position", [-107.4, 115.1, 0.0, -2.7, -2.7, 0.0])
    _assert_position(children[1], "Static position",
                     [-107.4, 115.11, -0.0013136, -2.7003, -2.6985, 0.0021886])

    total = children[26].signals
    assert len(total) == 7
    _assert_item(total[0], "Fx", FACTOR * 4.3415)
    _assert_item(total[6], "Mz", FACTOR * 68.857)

    element = children[27].signals
    assert len(element) == 7
    _assert_item(element[1], "Fx", FACTOR * 2829.6)
    _assert_item(element[2], "Fy", FACTOR * -2888.4)
    _assert_item(element[3], "Fz", FACTOR * -5587.0)
    fx, fy, fz = (_value(s) for s in element[1:4])
    assert _value(element[0]) == (fx**2 + fy**2 + fz**2) ** 0.5

    s7000 = static.containers[1]
    assert s7000.attributes["body"] == "S7000"
    s7000_children = s7000.containers
    assert len(s7000_children) == 39

    coupling = s7000_children[27].signals
    assert len(coupling) == 7
    _assert_item(coupling[1], "Fx", FACTOR * 197.85)
    _assert_item(coupling[6], "Mz", FACTOR * -14575)

    specified = children[42].signals
    assert len(specified) == 7
    _assert_item(specified[1], "Fx", FACTOR * 960.45)
    _assert_item(specified[6], "Mz", 0.0)

    first, last = s7000_children[33].signals, s7000_children[38].signals
    assert len(first) == len(last) == 7
    _assert_item(first[1], "Fx", FACTOR * -0.32791e-08)
    _assert_item(first[6], "Mz", FACTOR * 5.6262)
    _assert_item(last[1], "Fx", FACTOR * -19.375)
    _assert_item(last[6], "Mz", FACTOR * 471.10)


def _assert_position(container: Container, name: str, expected: list[float]) -> None:
    assert container.name == name
    assert len(container.signals) == 6
    assert [_value(s) for s in container.signals] == expected


def _assert_item(signal: Signal, name: str, value: float) -> None:
    assert signal.name == name
    assert _value(signal) == value


# -- SIMA's StaticConditionResultParserTest ---------------------------------

DELTA = 1e-10

BODY_FORCES = [
    "Gravity", "Time dependent mass", "Retardation function", "Hydrostatics",
    "Linear damping", "Quadratic damping", "First order wave", "Wind forces",
    "Linear current", "Quadratic current", "Distributed forces,slamming",
    "Distributed forces,volume", "Distributed forces,wave/current",
    "Second order wave drift, wind", "Wave drift damping", "Coupling forces",
    "Specified forces", "External forces", "Positioning elements", "Thruster",
    "Small body hydrodynamics", "Rigid body kinetics", "Slender system connection",
    "Second order wave drift, swell", "Total",
]


def _components(container: Container) -> list[float]:
    """Fx, Fy, Fz, Mx, My, Mz, whichever order the container holds them in."""
    values = {s.name: _value(s) for s in container.signals}
    return [values[name] for name in ("Fx", "Fy", "Fz", "Mx", "My", "Mz")]


def test_parsing():
    """StaticConditionResultParserTest.testParsing and testBodyForces, as far as the tree shows.

    Not in the tree, so not here: the header, date tag and file part, the
    position comparison, the coupling and branch of each coupling result, and
    the mass behind ``testThatGravityAccellerationIsCalculatedCorrect``.
    """
    static = _static(PARSER / "psc.lis")
    assert [b.name for b in static.containers] == ["TROLLC", "S7000", "FRAM", "HOOKS", "HOOKP"]

    trollc = static.container("TROLLC")
    position = [_value(s) for s in trollc.container("Static position").signals]
    assert position == pytest.approx([-118.0, 115.0, 0.0, -2.7, -2.7, 0.0], abs=DELTA)

    names = [c.name for c in trollc.containers]
    assert names[2:27] == BODY_FORCES
    assert _components(trollc.containers[2 + 13]) == pytest.approx(
        [47.4e3, 0.236e2, 0.0, 0.0, 0.0, 0.777e3], abs=DELTA)
    assert names[27:31] == ["line1", "line2", "line3", "line4"]
    assert names[31:] == ["TROLLC_SF_1", "TROLLC_SF_2", "TROLLC_SF_3", "TROLLC_SM_1"]
    assert _components(trollc.container("TROLLC_SF_1")) == pytest.approx(
        [0.0, 0.0, 0.322e8, 0.0, -0.736e9, 0.0], abs=DELTA)

    s7000 = static.container("S7000")
    position = [_value(s) for s in s7000.container("Static position").signals]
    assert position == pytest.approx([-80.2, 0.0, 0.0, 0.0, 0.0, 0.0], abs=DELTA)
    couplings = s7000.containers[27:]
    assert [c.name for c in couplings] == ["LIFTWS", "LIFTWP"]
    fx, fy, fz, mx, my, mz = _components(couplings[0])
    assert [fx, fy, fz, mx, my, mz] == pytest.approx(
        [244e3, -349e3, -0.526e7, -0.396e9, -0.585e7, -0.180e8], abs=DELTA)
    assert _value(couplings[0].signal("FTotal")) == pytest.approx(
        (fx**2 + fy**2 + fz**2) ** 0.5, abs=DELTA)

    hooks = static.container("HOOKS")
    assert [c.name for c in hooks.containers[27:]] == ["LIFTWS", "swc4", "mwc_part2"]
    assert static.container("HOOKP").containers[-1].name == "swc3"


# -- what a scan offers -----------------------------------------------------


def _touch(folder: Path, *names: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for name in names:
        (folder / name).write_bytes(b"")
    return folder


def _described(folder: Path) -> dict[str, list[str]]:
    return {e.name: [r.file for r in e.results] for e in scan.describe(folder).entries}


def test_only_psc_lis_is_claimed_among_the_listings():
    assert isinstance(find_reader(Path("psc.lis")), PscReader)
    assert isinstance(find_reader(Path("PSC-sima.lis")), PscReader)
    assert find_reader(Path("prs.lis")) is None
    assert find_reader(Path("prd.lis")) is None


def test_beside_a_static_result_psc_lis_is_static(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition",
                    "simo-static-results.h5", "psc.lis", "prs.lis", "prd.lis")

    assert _described(folder) == {"Static": ["simo-static-results.h5", "psc.lis"]}


def test_beside_a_riflex_static_result_psc_lis_is_static(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition", "sima_stamod.mpf", "psc-sima.lis")

    assert _described(folder) == {"Static": ["sima_stamod.mpf", "psc-sima.lis"]}


def test_in_a_dynamic_folder_psc_lis_is_the_static_runs_copy(tmp_path):
    """SIMORunner copies psc.lis into the dynamic working directory."""
    folder = _touch(tmp_path / "Task" / "Condition",
                    "simo-dynamic-results.h5", "psc.lis", "prd.lis")

    assert _described(folder) == {"Dynamic": ["simo-dynamic-results.h5"]}


def test_psc_lis_alone_is_not_a_run(tmp_path):
    folder = _touch(tmp_path / "Task" / "Condition", "psc.lis", "simores.inp")

    assert not holds_results(folder)
    with pytest.raises(ResultsError, match="holds no result files"):
        open_results(folder)


def test_directories_read_psc_lis_from_the_static_folder_only(tmp_path):
    """With ``directories`` the analysis is known, so the same-folder rule does not apply."""
    condition = tmp_path / "Heavy_Lifting_Operation" / "Initial"
    shutil.copytree(RUN, condition / "1-static")
    dynamic = condition / "1-dynamic"
    dynamic.mkdir()
    for name in ("psc.lis", "simores.inp"):
        shutil.copy(RUN / name, dynamic / name)
    (condition / "results.json").write_text(json.dumps(
        {"task": "Heavy_Lifting_Operation", "condition": "Initial",
         "directories": {"Static": "1-static", "Dynamic": "1-dynamic"}}), encoding="utf-8")

    res = open_results(condition)

    assert [s.file for s in res.sources] == ["1-static/psc.lis"]
    _assert_matches_oracle(res.run.container("Static"))


# -- damaged runs -----------------------------------------------------------


def test_without_simores_inp_the_source_fails(tmp_path):
    shutil.copy(RUN / "psc.lis", tmp_path / "psc.lis")

    with pytest.warns(UserWarning, match="simores.inp"):
        res = open_results(tmp_path / "psc.lis")

    assert [s.status for s in res.sources] == [Status.FAILED]
    assert "SourceError" in res.sources[0].detail
    marker = res.run.container("Static").signals[0]
    assert isinstance(marker, ErrorSignal)
    assert "simores.inp" in str(marker.error)


def _read(folder: Path) -> Container:
    into = Container("Static")
    PscReader().read(Source(path=folder / "psc.lis", context=FolderContext(folder=folder)), into)
    return into


def _damaged(tmp_path: Path, edit) -> Path:
    shutil.copy(RUN / "simores.inp", tmp_path / "simores.inp")
    lines = (RUN / "psc.lis").read_text(encoding="latin-1").splitlines()
    (tmp_path / "psc.lis").write_text("\n".join(edit(lines)) + "\n", encoding="latin-1")
    return tmp_path


def test_a_truncated_psc_lis_is_a_source_error(tmp_path):
    folder = _damaged(tmp_path, lambda lines: lines[:100])

    with pytest.raises(SourceError, match=r"psc\.lis line 100: the file ends early"):
        _read(folder)


def test_a_short_force_row_is_a_source_error_naming_the_line(tmp_path):
    def drop_a_value(lines):
        lines[16] = " ".join(lines[16].split()[:5])
        return lines

    with pytest.raises(SourceError, match=r"psc\.lis line 17: a body force should hold 6 values, found 5"):
        _read(_damaged(tmp_path, drop_a_value))


def test_a_body_simores_inp_does_not_name_is_a_source_error(tmp_path):
    def renumber(lines):
        lines[7] = "  9"
        return lines

    with pytest.raises(SourceError, match="no result for the body Platform"):
        _read(_damaged(tmp_path, renumber))


def test_specified_forces_simores_inp_does_not_name_are_a_source_error(tmp_path):
    def count_four(lines):
        lines[13] = "      8     11      0      0      4      0"
        return lines

    with pytest.raises(SourceError, match="4 specified forces on body Platform, but simores.inp names 3"):
        _read(_damaged(tmp_path, count_four))


def test_a_malformed_psc_lis_fails_its_source_only(copy_run):
    run = copy_run(RUN, {"psc.lis": b"SIMO_PSC_FILE\n02-OCT-2026 09:07\nSFOR\nfive\n"})

    with pytest.warns(UserWarning, match="expected an integer, found 'five'"):
        res = open_results(run / "psc.lis")

    assert [s.status for s in res.sources] == [Status.FAILED]

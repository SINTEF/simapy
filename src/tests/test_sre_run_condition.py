"""Running a condition and getting results back, without SRE command strings.

What is under test is the translation: arguments in, SIMA commands out, and the
condition opened afterwards. SIMA itself is not run -- these tests stand in
for it, so they say nothing about whether SIMA accepts the commands. That is
what the examples running against a real SRE are for.
"""

import json
import shutil
import subprocess
import threading
from pathlib import Path

import pytest

from simapy.results import ResultsError

DATA = Path(__file__).parent / "data"
RIFLEX_RUN = DATA / "Simple_Flexible_Riser" / "Initial"


def _leave_results(folder: Path) -> Path:
    """Put a static result and its id map in ``folder``, as a solver would."""
    folder.mkdir(parents=True, exist_ok=True)
    for name in ("sima_stamod.mpf", "names.map"):
        shutil.copyfile(RIFLEX_RUN / name, folder / name)
    return folder


def _sima_writes(task: str = "T", condition: str = "C", run: str = "1-20260901083636",
                 members: tuple[str, ...] = ()):
    """A stand-in run: results in ``run``, and the results.json SIMA writes beside them."""

    def on_run(working_dir: Path):
        root = working_dir / task / condition
        content = {"task": task, "condition": condition,
                   "variables": {"hs": {"value": 1.5, "unit": "m"}}}
        if members:
            content["conditions"] = [
                {"condition": member, "variables": {"kzz": {"value": float(n), "unit": "N*m"}},
                 "directories": {"Static": f"{run}/{member}"}}
                for n, member in enumerate(members, start=1)]
            for member in members:
                _leave_results(root / run / member)
        else:
            content["directories"] = {"Static": run}
            _leave_results(root / run)
        (root / "results.json").write_text(json.dumps(content), encoding="utf-8")

    return on_run


@pytest.fixture(name="ran")
def ran_fixture(sima):
    """A SIMA whose run leaves a plain condition T/C behind."""
    sima.on_run = _sima_writes()
    return sima


def test_builds_an_import_and_a_condition_run(ran, tmp_path):
    ran.run_condition(tmp_path / "ws", stask=tmp_path / "model.stask",
                      task="T", condition="C", run_type="static")

    assert ran.recorded["commands"] == [
        {"type": "sima/command/ImportCommand", "file": str((tmp_path / "model.stask").absolute())},
        {"type": "sima/command/ConditionRunCommand", "task": "T", "condition": "C",
         "runType": "static"},
    ]
    assert ran.recorded["arguments"][-2:] == [
        "--commands", f"file={(tmp_path / 'ws' / 'commands.json').absolute()}"]


def test_a_stask_is_optional(ran, tmp_path):
    """The workspace may already hold the task, so importing is a choice."""
    ran.run_condition(tmp_path / "ws", task="T", condition="C")

    assert set(ran.recorded["by_type"]) == {"ConditionRunCommand"}


def test_variables_become_properties(ran, tmp_path):
    """A dict is the Python shape; SIMA wants key/value pairs as strings."""
    ran.run_condition(tmp_path / "ws", task="T", condition="C", variables={"Hs": 2.0, "Tp": 5})

    run = ran.recorded["by_type"]["ConditionRunCommand"]
    assert run["input"] == [
        {"type": "sima/sima/Property", "key": "Hs", "value": "2.0"},
        {"type": "sima/sima/Property", "key": "Tp", "value": "5"},
    ]


def test_no_variables_leaves_input_alone(ran, tmp_path):
    ran.run_condition(tmp_path / "ws", task="T", condition="C")
    assert not ran.recorded["by_type"]["ConditionRunCommand"].get("input")


def test_returns_the_condition(ran, tmp_path):
    res = ran.run_condition(tmp_path / "ws", task="T", condition="C")

    assert res.folder == (tmp_path / "ws" / "T" / "C").absolute()
    assert (res.run.name, res.run.type) == ("C", "condition")
    assert res.run["Variables/hs"].unit == "m"
    assert "Static/RiserLine" in res.run


def test_a_set_is_one_result_too(sima, tmp_path):
    """The set, then one condition per member, as SIMA's post processor shows it."""
    sima.on_run = _sima_writes(condition="Set", members=("Set_1", "Set_2"))

    res = sima.run_condition(tmp_path / "ws", task="T", condition="Set")

    assert (res.run.name, res.run.type) == ("Set", "conditionContainer")
    members = [c for c in res.run.containers if c.type == "condition"]
    assert [m.name for m in members] == ["Set_1", "Set_2"]
    assert members[1]["Variables/kzz"].y[0] == 2.0


def test_without_results_json_is_an_error(sima, tmp_path):
    """SIMA before 5.4 writes none, and there is then no telling which runs are this one."""
    sima.on_run = lambda ws: _leave_results(ws / "T" / "C" / "1-20260901083636")

    with pytest.raises(ResultsError, match="results.json"):
        sima.run_condition(tmp_path / "ws", task="T", condition="C")


def test_a_failed_run_does_not_return_the_previous_one(sima, tmp_path):
    """With fail_on_error off, an untouched results.json still belongs to an earlier run."""
    sima.on_run = _sima_writes()
    sima.run_condition(tmp_path / "ws", task="T", condition="C")
    sima.on_run = lambda ws: None
    sima.fail_on_error = False
    sima.returncode = 1

    with pytest.raises(ResultsError, match="wrote no"):
        sima.run_condition(tmp_path / "ws", task="T", condition="C")


def test_a_rerun_reads_only_what_results_json_names(sima, tmp_path):
    sima.on_run = _sima_writes()
    sima.run_condition(tmp_path / "ws", task="T", condition="C")
    sima.on_run = _sima_writes(run="2-20260901090000")

    res = sima.run_condition(tmp_path / "ws", task="T", condition="C")

    assert [s.file for s in res.sources] == ["2-20260901090000/sima_stamod.mpf"]


class TestResultsDir:
    """Results copied out of the workspace read back as they did in it."""

    def test_the_copy_reads_as_the_condition(self, ran, tmp_path):
        out = tmp_path / "out"
        res = ran.run_condition(tmp_path / "ws", task="T", condition="C", results_dir=out)

        assert res.folder == out.absolute()
        assert (res.description.task, res.run.name) == ("T", "C")
        assert res.run["Variables/hs"].unit == "m"
        assert "Static/RiserLine" in res.run

    def test_sima_does_not_copy(self, ran, tmp_path):
        """SIMA's copy flattens the timestamp folder, so results.json would point nowhere."""
        ran.run_condition(tmp_path / "ws", task="T", condition="C", results_dir=tmp_path / "out")
        assert not ran.recorded["by_type"]["ConditionRunCommand"].get("copy")

    def test_only_results_and_what_names_them_are_copied(self, sima, tmp_path):
        def run(ws):
            _sima_writes()(ws)
            (ws / "T" / "C" / "1-20260901083636" / "stamod.inp").write_text("", encoding="utf-8")

        sima.on_run = run
        out = tmp_path / "out"
        sima.run_condition(tmp_path / "ws", task="T", condition="C", results_dir=out)

        assert sorted(p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()) == [
            "1-20260901083636/names.map", "1-20260901083636/sima_stamod.mpf", "results.json"]

    def test_a_set_keeps_its_members_apart(self, sima, tmp_path):
        sima.on_run = _sima_writes(condition="Set", members=("Set_1", "Set_2"))
        out = tmp_path / "out"

        res = sima.run_condition(tmp_path / "ws", task="T", condition="Set", results_dir=out)

        assert [c.name for c in res.run.containers if c.type == "condition"] == ["Set_1", "Set_2"]
        assert len(res.sources) == 2

    def test_earlier_copies_are_not_read(self, sima, tmp_path):
        out = tmp_path / "out"
        _leave_results(out / "0-20260801000000")
        sima.on_run = _sima_writes()

        res = sima.run_condition(tmp_path / "ws", task="T", condition="C", results_dir=out)

        assert [s.file for s in res.sources] == ["1-20260901083636/sima_stamod.mpf"]


class TestRun:
    """The process call underneath both run methods."""

    def test_output_is_kept_without_show_output(self, sima, tmp_path):
        sima.output = b"first\nbad \xff byte\n"
        sima.run_workflow(tmp_path / "ws", task="T", workflow="w")

        assert (tmp_path / "ws" / "stdout.txt").read_text(encoding="utf-8") == \
            "first\nbad \N{REPLACEMENT CHARACTER} byte\n"

    def test_nothing_waits_on_stdin(self, sima, tmp_path):
        sima.run_workflow(tmp_path / "ws", task="T", workflow="w")
        assert sima.recorded["popen"]["stdin"] is subprocess.DEVNULL

    def test_a_str_working_dir_works(self, ran, tmp_path):
        assert ran.run_condition(str(tmp_path / "ws"), task="T", condition="C").run.name == "C"

    def test_a_timeout_kills_the_process(self, sima, tmp_path, monkeypatch):
        killed = threading.Event()

        class Hanging:
            def __init__(self):
                self.stdout = self

            def readline(self):
                killed.wait(10)
                return b""

            def wait(self, timeout=None):
                return 1

            def kill(self):
                killed.set()

        monkeypatch.setattr(subprocess, "Popen", lambda *args, **kwargs: Hanging())
        with pytest.raises(subprocess.TimeoutExpired):
            sima.run(tmp_path / "ws", ["--help"], timeout=0.05)
        assert killed.is_set()

    def test_a_nonzero_exit_raises(self, sima, tmp_path):
        sima.returncode = 3
        with pytest.raises(RuntimeError, match="error code 3"):
            sima.run_workflow(tmp_path / "ws", task="T", workflow="w")

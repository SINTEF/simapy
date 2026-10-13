"""Running a workflow without SRE command strings.

What is under test is the translation: arguments in, SIMA commands out. SIMA
itself is not run -- these tests stand in for it, so they say nothing about
whether SIMA accepts the commands. That is what the SIMAPy examples in sima-doc,
run against a real SRE, are for.
"""


def test_builds_an_import_and_a_workflow_run(sima, tmp_path):
    sima.run_workflow(tmp_path / "ws", task="WorkflowTask", workflow="outer",
                      stask=tmp_path / "model.stask")

    commands = sima.recorded["by_type"]
    assert set(commands) == {"ImportCommand", "WorkflowRunCommand"}
    assert commands["ImportCommand"]["file"] == str((tmp_path / "model.stask").absolute())
    run = commands["WorkflowRunCommand"]
    assert (run["task"], run["workflow"]) == ("WorkflowTask", "outer")


def test_the_import_comes_first(sima, tmp_path):
    """A workflow cannot run from a task that has not been imported yet."""
    sima.run_workflow(tmp_path / "ws", task="T", workflow="w", stask=tmp_path / "model.stask")

    assert [c["type"] for c in sima.recorded["commands"]] == [
        "sima/command/ImportCommand", "sima/command/WorkflowRunCommand"]


def test_a_stask_is_optional(sima, tmp_path):
    """The workspace may already hold the task, so importing is a choice."""
    sima.run_workflow(tmp_path / "ws", task="T", workflow="w")

    assert set(sima.recorded["by_type"]) == {"WorkflowRunCommand"}


def test_variables_become_properties(sima, tmp_path):
    """A dict is the Python shape; SIMA wants key/value pairs as strings."""
    sima.run_workflow(tmp_path / "ws", task="T", workflow="w",
                      variables={"scale": 3.0, "runs": 5})

    run = sima.recorded["by_type"]["WorkflowRunCommand"]
    assert run["input"] == [
        {"type": "sima/sima/Property", "key": "scale", "value": "3.0"},
        {"type": "sima/sima/Property", "key": "runs", "value": "5"},
    ]


def test_no_variables_leaves_input_alone(sima, tmp_path):
    sima.run_workflow(tmp_path / "ws", task="T", workflow="w")
    assert not sima.recorded["by_type"]["WorkflowRunCommand"].get("input")


def test_the_working_directory_is_passed_through(sima, tmp_path):
    sima.run_workflow(str(tmp_path / "ws"), task="T", workflow="w")
    assert sima.recorded["working_dir"] == tmp_path / "ws"

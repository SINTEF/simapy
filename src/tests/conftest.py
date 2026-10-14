"""Shared helpers for the SRE tests."""

import io
import json
import subprocess
from pathlib import Path

import pytest

from simapy.sre import SIMA

#: Result files are fixtures of the simapy-results package; the SRE tests borrow them.
RESULTS_DATA = Path(__file__).parents[2] / "packages" / "simapy-results" / "tests" / "data"


class _FakeProcess:
    """What ``SIMA.run`` reads from a process: its output and its exit code."""

    def __init__(self, output: bytes, returncode: int):
        self.stdout = io.BytesIO(output)
        self.returncode = returncode

    def wait(self, timeout=None):
        return self.returncode

    def kill(self):
        pass


@pytest.fixture(name="sima")
def sima_fixture(tmp_path, monkeypatch):
    """A SIMA whose process is faked, so its commands still go through ``commands.json``.

    ``sima.on_run(working_dir)`` stands in for the run and may leave result
    files behind; ``sima.output`` and ``sima.returncode`` are what the process
    reports. ``sima.recorded`` holds what the process was given: ``working_dir``,
    ``arguments``, the ``popen`` keyword arguments, the ``commands`` read back
    from the file, and the same keyed by type name as ``by_type``.

    The executable check is the only reason a SIMA cannot be built without one
    installed, so it points at a file that exists.
    """
    exe = tmp_path / "sre"
    exe.write_text("", encoding="utf-8")
    instance = SIMA(exe=str(exe), show_output=False)
    instance.recorded = {}
    instance.on_run = lambda working_dir: None
    instance.output = b""
    instance.returncode = 0

    def popen(arguments, **kwargs):
        working_dir = Path(arguments[arguments.index("-data") + 1])
        file = Path(arguments[arguments.index("--commands") + 1].split("=", 1)[1])
        commands = json.loads(file.read_text(encoding="utf-8"))["contents"]
        instance.recorded.update(
            working_dir=working_dir, arguments=list(arguments), popen=kwargs,
            commands=commands,
            by_type={c["type"].rsplit("/", 1)[-1]: c for c in commands},
        )
        instance.on_run(working_dir)
        return _FakeProcess(instance.output, instance.returncode)

    monkeypatch.setattr(subprocess, "Popen", popen)
    return instance

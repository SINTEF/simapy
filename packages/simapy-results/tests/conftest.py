"""Shared helpers for the results tests."""

import shutil
from pathlib import Path

import numpy as np
import pytest

from simapy_results import Signal
from simapy_results._readers import mpf

DATA = Path(__file__).parent / "data"


class ArrayValues:
    """Values held in memory, for trees built by hand."""

    def __init__(self, x, y):
        self._x = np.asarray(x, dtype=np.float64)
        self._y = np.asarray(y, dtype=np.float64)

    @property
    def size(self) -> int:
        return len(self._x)

    def x(self):
        return self._x

    def y(self):
        return self._y


def array_signal(name: str, x=(), y=(), unit: str | None = "-", xunit: str | None = "m",
                 **attributes: str) -> Signal:
    """A signal over in-memory arrays; empty unless given values."""
    return Signal(name, ArrayValues(x, y), unit=unit, xunit=xunit, **attributes)


@pytest.fixture(name="parses")
def parses_fixture(monkeypatch):
    """Every mpf block parsed while the test runs, in order."""
    parses = []
    original = mpf._Block._parse
    monkeypatch.setattr(
        mpf._Block, "_parse", lambda self: parses.append(self) or original(self)
    )
    return parses


@pytest.fixture(name="copy_run")
def copy_run_fixture(tmp_path):
    """Copy a fixture run folder into tmp_path, keeping its last two segments.

    The task and condition come from the folder path -- that is the whole point
    of reading a folder -- so a copy has to preserve ``<task>/<condition>`` or
    every path in the tree changes.
    """

    def copy(source: Path, extra: dict[str, bytes] | None = None) -> Path:
        source = Path(source)
        run = tmp_path / source.parent.name / source.name
        run.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, run)
        for name, content in (extra or {}).items():
            (run / name).write_bytes(content)
        return run

    return copy


@pytest.fixture(name="variables_inp")
def variables_inp_fixture():
    """Build a ``variables.inp`` the way ``createVariableFile`` writes one.

    One block per model reference, each naming the task and the reference it
    came from -- the reference is what types the values.
    """

    def build(task: str = "Task", **blocks: dict[str, object]) -> bytes:
        lines: list[str] = []
        for reference, values in blocks.items():
            lines.append(f"'{task}.{reference}")
            lines.append("'Number of variables")
            lines.append(str(len(values)))
            lines.append("'Variable=Value")
            lines.extend(f"{name}={value}" for name, value in values.items())
        return ("\n".join(lines) + "\n").encode("utf-8")

    return build

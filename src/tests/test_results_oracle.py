"""The tree simapy builds must match the tree SIMA builds.

``riflex_run_oracle.json`` is a snapshot of ``Riflex_Results.h5``, which the
PostProcessorTask in the TestWs workspace wrote from this exact run. Container
shape, signal names, units, lengths and end values all come from there.

``segment_*`` subtrees are excluded from the snapshot: those come from the
``.bin`` storage reader, which is out of scope.
"""

import json

import numpy as np
import pytest

from simapy.results import Container, Signal, Status, open_results

from .conftest import DATA

RUN = DATA / "Simple_Flexible_Riser" / "Initial"

# The H5 mangles '.' out of dataset names; simapy keeps the real name.
MANGLED = str.maketrans({".": "_"})


@pytest.fixture(scope="module", name="oracle")
def oracle_fixture():
    return json.loads((DATA / "riflex_run_oracle.json").read_text())


@pytest.fixture(scope="module", name="condition")
def condition_fixture():
    return open_results(RUN)["Initial"]


def test_every_result_file_was_read():
    res = open_results(RUN)
    assert [s.status for s in res.sources] == [Status.READ, Status.READ]
    assert res.name == "Simple_Flexible_Riser"
    assert res.type == "task"


def test_container_shape_matches_oracle(condition, oracle):
    for expected in oracle["containers"]:
        node = condition[expected["path"]]
        assert node.type == expected["type"], expected["path"]

        # Oracle children carry the H5-mangled names, and segments are absent.
        actual = {name.translate(MANGLED) for name in node.keys()}
        wanted = {
            name for name in expected["children"] if not name.startswith("segment_")
        }
        assert wanted <= actual, expected["path"]


def test_no_unexpected_containers(condition, oracle):
    """The tree has exactly the containers SIMA's export has, and no others."""
    expected = {c["path"] for c in oracle["containers"]}
    # Paths are rooted at the task; the oracle is rooted at the condition.
    prefix = f"{condition.name}/"
    actual = {
        n.path.removeprefix(prefix)
        for n in condition.walk()
        if isinstance(n, Container)
    }
    assert actual == expected


def test_signal_metadata_matches_oracle(condition, oracle):
    """Names, units and lengths, all from SIMA's own export."""
    for expected in oracle["signals"]:
        signal = _signal(condition, expected)
        assert signal.name == expected["name"]
        assert signal.unit == expected["yunit"]
        assert signal.xunit == expected["xunit"]
        assert len(signal) == expected["n"]


def test_signal_values_match_oracle(condition, oracle):
    """First and last three samples of every signal."""
    for expected in oracle["signals"]:
        signal = _signal(condition, expected)
        where = f"{expected['container']}/{expected['name']}"
        _close(signal.x[:3], expected["x_head"], f"{where} x head")
        _close(signal.x[-3:], expected["x_tail"], f"{where} x tail")
        _close(signal.y[:3], expected["y_head"], f"{where} y head")
        _close(signal.y[-3:], expected["y_tail"], f"{where} y tail")


def test_signal_count_matches_oracle(condition, oracle):
    """Nothing extra, nothing missing."""
    actual = [n for n in condition.walk() if isinstance(n, Signal)]
    assert len(actual) == len(oracle["signals"])


def _signal(condition, expected) -> Signal:
    return condition.container(expected["container"]).signal(expected["name"])


def _close(actual, expected, where):
    # RIFLEX writes 7 significant digits; SIMA stores float64 of the same text.
    assert np.allclose(actual, expected, rtol=1e-9, atol=0), (
        f"{where}: {list(actual)} != {expected}"
    )

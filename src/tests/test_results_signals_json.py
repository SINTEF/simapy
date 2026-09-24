"""Opening a workflow's output: one named file, in either format.

A workflow's file output node writes one file rather than filling a folder, so
it is opened by name. The point of the tests is that naming it gives the same
tree the folder would: same containers, same units, same values.
"""

import json

import numpy as np
import pytest

from simapy.results import (
    Container,
    ResultsError,
    Signal,
    Status,
    open_results,
)
from simapy.results._scan import find_runs, holds_results

MODEL = "sima/ModelContent"


def _document(*contents) -> dict:
    return {"type": MODEL, "header": {"type": "sima/Header"}, "contents": list(contents)}


def _container(name, *signals) -> dict:
    return {"name": name, "type": "sima/signals/Container", "signals": list(signals)}


def _equally_spaced(name, values, xstart=0.0, xdelta=0.1, unit="m", xunit="s") -> dict:
    return {
        "name": name, "type": "sima/signals/EquallySpacedSignal",
        "xstart": xstart, "xdelta": xdelta, "value": list(values),
        "unit": unit, "xunit": xunit,
    }


def _signal_paths(container: Container) -> list[str]:
    return [node.path for node in container.walk() if isinstance(node, Signal)]


def _write(folder, name, document):
    path = folder / name
    path.write_text(json.dumps(document), encoding="utf-8")
    return path


@pytest.fixture(name="out")
def out_fixture(tmp_path):
    """A workflow output holding one container with two signals."""
    return _write(tmp_path, "out.json", _document(_container(
        "some_data",
        _equally_spaced("height", [1.0, 2.0, 3.0]),
        {"name": "scale", "type": "sima/signals/DimensionalScalar", "value": 3.0, "unit": "-"},
    )))


def test_a_file_opens_as_a_tree(out, tmp_path):
    res = open_results(out)

    assert _signal_paths(res) == [
        f"{tmp_path.name}/some_data/height", f"{tmp_path.name}/some_data/scale"]


def test_values_units_and_axis_survive(out, tmp_path):
    height = open_results(out).signal(f"{tmp_path.name}/some_data/height")

    assert (height.unit, height.xunit) == ("m", "s")
    assert np.array_equal(height.y, [1.0, 2.0, 3.0])
    assert np.array_equal(height.x, [0.0, 0.1, 0.2])
    assert height.is_equidistant


def test_a_scalar_is_one_sample(out, tmp_path):
    scale = open_results(out).signal(f"{tmp_path.name}/some_data/scale")

    assert len(scale) == 1
    assert np.array_equal(scale.y, [3.0])


def test_an_explicit_x_axis_is_kept(tmp_path):
    path = _write(tmp_path, "out.json", _document(_container("c", {
        "name": "uneven", "type": "sima/signals/NonEquallySpacedSignal",
        "xvalue": [0.0, 1.0, 4.0], "value": [1.0, 2.0, 3.0], "unit": "m", "xunit": "s",
    })))

    signal = open_results(path).signal(f"{tmp_path.name}/c/uneven")
    assert not signal.is_equidistant
    assert np.array_equal(signal.x, [0.0, 1.0, 4.0])


def test_containers_nest(tmp_path):
    inner = _container("inner", _equally_spaced("y", [1.0]))
    outer = {"name": "outer", "type": "sima/signals/Container",
             "signals": [], "containers": [inner]}
    path = _write(tmp_path, "out.json", _document(outer))

    assert _signal_paths(open_results(path)) == [f"{tmp_path.name}/outer/inner/y"]


def test_a_document_with_no_signals_reads_as_nothing(tmp_path):
    """commands.json is a valid model. It is just not results."""
    path = _write(tmp_path, "commands.json", _document(
        {"type": "sima/command/ImportCommand", "file": "model.stask"}))

    res = open_results(path)
    assert _signal_paths(res) == []
    assert [(s.file, s.signals) for s in res.sources] == [("commands.json", 0)]


def test_malformed_json_is_reported_not_raised(tmp_path):
    """A source that cannot be read lands in sources, as for any other format."""
    path = tmp_path / "out.json"
    path.write_text("{not json", encoding="utf-8")

    with pytest.warns(UserWarning, match="not valid JSON"):
        res = open_results(path)
    assert res.sources[0].status is Status.FAILED


def test_units_are_converted_into_base_units(tmp_path):
    path = _write(tmp_path, "out.json", _document(_container(
        "c", _equally_spaced("force", [1.0, 2.0], unit="kN", xunit="s"))))

    force = open_results(path).signal(f"{tmp_path.name}/c/force")

    assert force.unit == "N"
    assert np.array_equal(force.y, [1000.0, 2000.0])


def test_json_and_hdf5_agree_on_units_and_values(tmp_path):
    """The same signal written in either format reads as the same signal."""
    h5py = pytest.importorskip("h5py")
    json_path = _write(tmp_path, "out.json", _document(_container(
        "c", _equally_spaced("force", [1.0, 2.0, 3.0], xdelta=0.5, unit="kN", xunit="s"))))
    h5_path = tmp_path / "out.h5"
    with h5py.File(h5_path, "w") as handle:
        dataset = handle.create_group("c").create_dataset("force", data=[1.0, 2.0, 3.0])
        dataset.attrs.update({"yunit": b"kN", "xunit": b"s", "delta": 0.5, "start": 0.0})

    from_json = open_results(json_path).signal(f"{tmp_path.name}/c/force")
    from_h5 = open_results(h5_path).signal(f"{tmp_path.name}/c/force")

    assert (from_json.unit, from_json.xunit) == (from_h5.unit, from_h5.xunit) == ("N", "s")
    assert np.array_equal(from_json.y, from_h5.y)
    assert np.array_equal(from_json.x, from_h5.x)


def test_values_cannot_be_altered_through_a_signal(out, tmp_path):
    height = open_results(out).signal(f"{tmp_path.name}/some_data/height")

    with pytest.raises(ValueError, match="read-only"):
        height.y[0] = 99.0
    assert np.array_equal(height.y, [1.0, 2.0, 3.0])


def test_a_null_axis_falls_back_to_the_defaults(tmp_path):
    signal = _equally_spaced("y", [1.0, 2.0])
    signal.update(xstart=None, xdelta=None)
    path = _write(tmp_path, "out.json", _document(_container("c", signal)))

    y = open_results(path).signal(f"{tmp_path.name}/c/y")

    assert (y.xstart, y.xdelta) == (0.0, 1.0)


def test_attributes_are_carried_and_cannot_shadow_the_fields(tmp_path):
    signal = _equally_spaced("y", [1.0], unit="kN")
    signal["attributes"] = [
        {"name": "legend", "value": "Tension"},
        {"name": "unit", "value": "furlong"},
        {"name": "name", "value": "other"},
    ]
    path = _write(tmp_path, "out.json", _document(_container("c", signal)))

    y = open_results(path).signal(f"{tmp_path.name}/c/y")

    assert y.attributes["legend"] == "Tension"
    assert (y.name, y.unit) == ("y", "N")


def test_arrays_read_on_a_sample_index(tmp_path):
    path = _write(tmp_path, "out.json", _document(_container(
        "c",
        {"name": "counts", "type": "sima/signals/IntegerArray", "value": [3, 1, 4]},
        {"name": "flags", "type": "sima/signals/BooleanArray", "value": [True, False]},
    )))
    res = open_results(path)

    counts = res.signal(f"{tmp_path.name}/c/counts")
    assert np.array_equal(counts.x, [0.0, 1.0, 2.0])
    assert np.array_equal(counts.y, [3.0, 1.0, 4.0])
    assert np.array_equal(res.signal(f"{tmp_path.name}/c/flags").y, [1.0, 0.0])


def test_text_stays_text(tmp_path):
    path = _write(tmp_path, "out.json", _document(_container(
        "c",
        {"name": "comment", "type": "sima/signals/SimpleString", "value": "calm sea"},
        {"name": "labels", "type": "sima/signals/StringArray", "value": ["a", "b"]},
    )))
    res = open_results(path)

    assert res.signal(f"{tmp_path.name}/c/comment").y.tolist() == ["calm sea"]
    assert res.signal(f"{tmp_path.name}/c/labels").y.tolist() == ["a", "b"]


def test_a_file_no_reader_claims_is_an_error(tmp_path):
    """A scan may pass over a file; a caller who named one is owed an answer."""
    path = tmp_path / "notes.txt"
    path.write_text("", encoding="utf-8")

    with pytest.raises(ResultsError, match="no reader"):
        open_results(path)


def test_a_missing_path_is_an_error(tmp_path):
    with pytest.raises(ResultsError, match="not a directory or a file"):
        open_results(tmp_path / "nowhere")


class TestScansIgnoreJson:
    """Registering a json reader must not change what a folder looks like.

    A workflow writes its input and its output as the same signals model in the
    same folder, and `SIMA.run` leaves commands.json beside them. Nothing in
    such a file says which it is, so a scan cannot choose and does not try.
    """

    def test_a_folder_of_json_holds_no_results(self, tmp_path):
        _write(tmp_path, "out.json", _document(_container("c", _equally_spaced("y", [1.0]))))
        _write(tmp_path, "input.json", _document(_container("c", _equally_spaced("a", [1.0]))))

        assert not holds_results(tmp_path)

    def test_a_run_folder_is_not_invented_by_json(self, tmp_path):
        run = tmp_path / "1-20260901083937"
        run.mkdir()
        _write(run, "commands.json", _document())

        assert find_runs(tmp_path) == []

    def test_opening_the_folder_reads_no_json(self, tmp_path):
        _write(tmp_path, "out.json", _document(_container("c", _equally_spaced("y", [1.0]))))

        with pytest.raises(ResultsError, match="holds no result files"):
            open_results(tmp_path)


def test_a_container_keeps_its_type_and_attributes(tmp_path):
    """As SIMA exports a body: the type and the body name are container attributes."""
    body = _container("Platform", _equally_spaced("x", [1.0]))
    body["attributes"] = [{"type": "sima/signals/Attribute", "name": "type", "value": "body"},
                          {"type": "sima/signals/Attribute", "name": "body", "value": "Platform"}]
    path = _write(tmp_path, "out.json", _document(body))

    platform = open_results(path).run.container("Platform")

    assert (platform.type, platform.attributes["body"]) == ("body", "Platform")

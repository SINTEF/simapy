"""HDF5 results, and the equally-spaced signals that only HDF5 produces.

The fixture is ``ts_buffer.b5`` from a SIMO run: 73 rank-1 datasets carrying a
``delta`` attribute and no x-axis anywhere in the file. That is what makes it the
right test for equidistant handling -- an mpf cannot express it.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

from simapy.results import Container, Signal, Status, open_results
from simapy.results._readers import hdf5
from simapy.results._sources import FolderContext, Source, SourceError

h5py = pytest.importorskip("h5py")

DATA = Path(__file__).parent / "data"
RUN = DATA / "Heavy_Lifting_Operation" / "Initial"

POSITION = "Initial/Dynamic/Platform/Global total position"
XG = f"{POSITION}/XG translation"
MOORING = "Initial/Dynamic/Platform/Positioning elements/MooringLine1/Total force"


# -- the SIMO tree ---------------------------------------------------------


def test_the_run_reads():
    res = open_results(RUN)

    assert res.name == "Heavy_Lifting_Operation"
    assert [s.status for s in res.sources] == [Status.READ]
    assert res.sources[0].signals == 73


def test_bodies_are_the_top_level():
    """Bodies sit directly under the analysis, typed body."""
    dynamic = open_results(RUN)["Initial/Dynamic"]

    assert [c.name for c in dynamic.containers] == [
        "Platform",
        "Lifter",
        "Module",
        "HookStarboard",
        "HookPort",
        "Origo",
    ]
    assert dynamic["Platform"].type == "body"
    assert open_results(RUN).find(type="body")[0].name == "Platform"


def test_the_tree_goes_body_category_element_signal():
    res = open_results(RUN)

    assert res[MOORING].name == "Total force"
    assert [c.name for c in res["Initial/Dynamic/Platform"].containers] == [
        "Wave elevation",
        "Positioning elements",
        "Couplings",
        "Global total position",
    ]


def test_dispatch_reached_the_reader_by_extension():
    """SIMA registers this file as simo_ts_buffer, which no reader claims.

    A folder cannot supply that label anyway, so the extension is the only
    stage there is -- and it is the one findImporter falls back to.
    """
    res = open_results(RUN)

    assert [s.type for s in res.sources] == ["b5"]
    assert res.sources[0].status is Status.READ


# -- equally spaced --------------------------------------------------------


def test_a_rank_1_dataset_with_delta_is_equidistant():
    signal = open_results(RUN)[XG]

    assert signal.is_equidistant
    assert signal.xstart == 0.0
    assert signal.xdelta == pytest.approx(0.1)
    assert signal.xunit == "s"
    assert len(signal) == 100


def test_the_x_axis_is_synthesised_not_stored():
    signal = open_results(RUN)[XG]

    assert signal.x[:4] == pytest.approx([0.0, 0.1, 0.2, 0.3])
    assert signal.x[-1] == pytest.approx(9.9)
    # A fresh array each time, so nothing is retained between calls.
    assert signal.x is not signal.x


def test_sharing_an_axis_costs_no_reads(monkeypatch):
    reads = []
    monkeypatch.setattr(
        hdf5._Dataset,
        "read",
        lambda self, item=Ellipsis: reads.append(self.name) or np.zeros(100),
    )

    position = open_results(RUN)[POSITION]
    assert position.signals[0].same_axis(position.signals[3])
    assert reads == []


def test_metadata_costs_no_reads(monkeypatch):
    reads = []
    monkeypatch.setattr(
        hdf5._Dataset,
        "read",
        lambda self, item=Ellipsis: reads.append(self.name) or np.zeros(100),
    )

    res = open_results(RUN)
    signals = [n for n in res.walk() if isinstance(n, Signal)]

    assert len(signals) == 73
    assert all(len(s) == 100 and s.xunit == "s" for s in signals)
    assert reads == []


def test_values_are_read_on_access():
    signal = open_results(RUN)[XG]

    assert signal.y[:2] == pytest.approx([-107.4069519, -107.4069443])
    assert signal.unit == "m"


def test_kn_becomes_newton():
    """yunit=kN in the file; the signals model stores base SI."""
    signal = open_results(RUN)[MOORING]

    assert signal.unit == "N"
    assert signal.y[0] == pytest.approx(6882337.89, rel=1e-6)


# -- frames over equidistant signals ---------------------------------------


def test_a_whole_body_frames_because_the_time_axis_is_shared():
    """73 signals, one time axis. Only possible because none of them stores x."""
    pytest.importorskip("pandas")
    frame = open_results(RUN)["Initial/Dynamic/Platform"].to_dataframe(recursive=True)

    assert frame.index.name == "time"
    assert frame.shape == (100, 26)  # 1 wave + 8 mooring + 11 couplings + 6 position
    assert list(frame.index[:3]) == pytest.approx([0.0, 0.1, 0.2])


def test_a_frame_keeps_units_per_column():
    pytest.importorskip("pandas")
    frame = open_results(RUN)[POSITION].to_dataframe()

    assert frame.attrs["units"]["XG translation"] == "m"
    assert frame.attrs["units"]["XB rotation"] == "deg"
    assert frame.attrs["xunit"] == "s"


# -- format dispatch -------------------------------------------------------


def test_a_simos_format_file_goes_to_the_other_reader(copy_run):
    """The root format attribute picks the layout, as SIMA does."""
    run = copy_run(RUN)
    with h5py.File(run / "other.h5", "w") as handle:
        handle.attrs["format"] = b"simos_r0"
        # Bare datasets at the root are not the simos layout, so the file reads
        # clean and yields nothing rather than being mangled into signals.
        handle.create_dataset("x", data=np.zeros(3))

    res = open_results(run)

    other = [s for s in res.sources if s.file == "other.h5"]
    assert [s.status for s in other] == [Status.READ]
    assert len(_signals(res)) == 73, "only ts_buffer.b5 contributes signals"


def test_a_file_with_no_format_uses_the_unformatted_reader(tmp_path):
    """The same bare root dataset the simos reader passes over is a signal here."""
    path = _write(tmp_path / "plain.h5", lambda handle: handle.create_dataset(
        "x", data=np.zeros(3)))

    assert [s.name for s in _read(path).signals] == ["x"]


# -- mangled names ---------------------------------------------------------


def test_the_name_attribute_beats_the_mangled_key(tmp_path):
    """HDF5 keys cannot hold a '.', so SIMA writes the true name alongside.

    In SIMA the name IS an attribute, so its import pass overwrites the mangled
    key implicitly. Here the name is a field, so it is promoted explicitly.
    """
    path = _write(
        tmp_path / "mangled.h5",
        lambda handle: _dataset(handle, "EFF_ TENSION", name=b"EFF. TENSION"),
    )

    signal = _read_one(path)

    assert signal.name == "EFF. TENSION"
    assert "name" not in signal.attributes


def test_a_group_recovers_its_true_name_too(tmp_path):
    def build(handle):
        group = handle.create_group("Mom_ about local y-axis")
        group.attrs["name"] = b"Mom. about local y-axis"
        _dataset(group, "MY")

    path = _write(tmp_path / "group.h5", build)
    container = _read(path)

    assert container.keys() == ["Mom. about local y-axis"]
    assert "name" not in container["Mom. about local y-axis"].attributes


def test_a_key_with_no_name_attribute_is_used_as_is(tmp_path):
    path = _write(tmp_path / "plain.h5", lambda handle: _dataset(handle, "MY"))

    assert _read_one(path).name == "MY"


def test_duplicate_true_names_stay_separate(tmp_path):
    """The exporter suffixes a colliding key with _duplicate_N.

    Both carry the same true name, and both must survive -- lookup by the
    mangled key is what keeps them apart while they are being built.
    """

    def build(handle):
        for key in ("Static forces", "Static forces_duplicate_1"):
            group = handle.create_group(key)
            group.attrs["name"] = b"Static forces"
            _dataset(group, "EFF_ TENSION", name=b"EFF. TENSION")

    container = _read(_write(tmp_path / "dup.h5", build))

    assert [c.name for c in container.containers] == ["Static forces", "Static forces"]


# -- short model ids -------------------------------------------------------


def test_a_group_named_by_a_short_id_is_resolved(tmp_path):
    """RIFLEX keys sima_elmfor.h5 groups by shortened model ids."""
    path = _write(tmp_path / "elmfor.h5", lambda handle: _dataset(
        handle.create_group("Moor1e20"), "Axial force"))

    container = _read(path, names={"Moor1e20": "MooringLine1"})

    assert container.keys() == ["MooringLine1"]


def test_a_group_name_that_is_not_an_id_is_left_alone(tmp_path):
    path = _write(tmp_path / "plain.h5", lambda handle: _dataset(
        handle.create_group("RiserLine"), "Axial force"))

    container = _read(path, names={"Moor1e20": "MooringLine1"})

    assert container.keys() == ["RiserLine"]


def test_resolution_is_exact_not_substring(tmp_path):
    """Eight-character ids would otherwise corrupt names that contain one."""
    path = _write(tmp_path / "sub.h5", lambda handle: _dataset(
        handle.create_group("Moor1e20_extra"), "Axial force"))

    container = _read(path, names={"Moor1e20": "MooringLine1"})

    assert container.keys() == ["Moor1e20_extra"]


# -- rank handling ---------------------------------------------------------


def test_rank_2_is_an_explicit_xy_pair(tmp_path):
    """The (2, N) shape SIMA writes when it exports a signal tree."""
    path = tmp_path / "xy.h5"
    with h5py.File(path, "w") as handle:
        data = handle.create_dataset("curve", data=np.array([[0.0, 2.0, 4.0], [1.0, 2.0, 3.0]]))
        data.attrs["xunit"] = b"m"
        data.attrs["yunit"] = b"kN"

    signal = _read_one(path)

    assert not signal.is_equidistant
    assert signal.x == pytest.approx([0.0, 2.0, 4.0])
    assert signal.y == pytest.approx([1000.0, 2000.0, 3000.0])
    assert (signal.xunit, signal.unit) == ("m", "N")


def test_rank_0_is_a_scalar(tmp_path):
    path = tmp_path / "scalar.h5"
    with h5py.File(path, "w") as handle:
        handle.create_dataset("mass", data=42.0).attrs["yunit"] = b"kg"

    signal = _read_one(path)

    assert len(signal) == 1
    assert signal.y == pytest.approx([42.0])
    assert signal.unit == "kg"


def test_rank_1_without_delta_falls_back_to_sample_numbers(tmp_path):
    path = tmp_path / "plain.h5"
    with h5py.File(path, "w") as handle:
        handle.create_dataset("plain", data=np.array([1.0, 2.0, 3.0]))

    signal = _read_one(path)

    assert not signal.is_equidistant
    assert signal.x == pytest.approx([0.0, 1.0, 2.0])


def test_non_textual_attributes_stay_out_of_the_metadata():
    """delta and start describe the axis; they are not attributes."""
    signal = open_results(RUN)[XG]

    assert "delta" not in signal.attributes
    assert signal.attributes["xunit"] == "s"


# -- strings ---------------------------------------------------------------


def test_a_variable_length_string_dataset_reads_as_str(tmp_path):
    path = _write(tmp_path / "text.h5", lambda handle: handle.create_dataset(
        "labels", data=["first", "second"], dtype=h5py.string_dtype()))

    assert _read_one(path).y.tolist() == ["first", "second"]


# -- environment -----------------------------------------------------------


def test_reading_without_h5py_names_the_missing_package(monkeypatch, tmp_path):
    path = _write(tmp_path / "plain.h5", lambda handle: _dataset(handle, "MY"))
    monkeypatch.setitem(sys.modules, "h5py", None)

    with pytest.raises(SourceError, match="h5py is required"):
        _read(path)


def test_a_run_without_h5py_reports_the_file_as_failed(monkeypatch):
    monkeypatch.setitem(sys.modules, "h5py", None)

    with pytest.warns(UserWarning, match="h5py is required"):
        res = open_results(RUN)

    assert [s.status for s in res.sources] == [Status.FAILED]
    assert "h5py is required" in res.sources[0].detail


# -- helpers ---------------------------------------------------------------


def _read(path: Path, names: dict | None = None) -> Container:
    container = Container("root")
    context = FolderContext(path.parent, names=names or {})
    hdf5.Hdf5Reader().read(Source(path=path, context=context), container)
    return container


def _read_one(path: Path) -> Signal:
    return _read(path).signals[0]


def _signals(container: Container) -> list[Signal]:
    return [node for node in container.walk() if isinstance(node, Signal)]


def _write(path: Path, build) -> Path:
    with h5py.File(path, "w") as handle:
        build(handle)
    return path


def _dataset(group, key: str, name: bytes | None = None):
    data = group.create_dataset(key, data=np.array([1.0, 2.0, 3.0]))
    if name is not None:
        data.attrs["name"] = name
    return data

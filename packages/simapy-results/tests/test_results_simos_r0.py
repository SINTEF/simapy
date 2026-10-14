"""The simos_r0 layout SIMO writes.

What is under test is the conversion, not the walk: metadata comes from child
datasets rather than attributes, containers are named by a ``name`` dataset, and
values are rescaled into base units. Every fixture here is built to the shapes
observed in real SIMO output -- `srv/Simo/ctest` and the coupled RIFLEX-SIMO
build trees -- so the member sets are the ones that actually occur.

The rescaling is the part worth pinning. SIMA divides by the
unit factor and reports the base unit, so a kN signal is served as N; reading the
datasets untouched would disagree with SIMA by a factor of 1000.
"""

import warnings
from pathlib import Path

import numpy as np
import pytest

from simapy_results import Container, ErrorSignal, Signal, open_results
from simapy_results._units import UNSCALED_ATTRIBUTE


def _signals(container: Container) -> list[Signal]:
    return [node for node in container.walk() if isinstance(node, Signal)]


def _string(handle, group, name, value):
    """A size-1 |S dataset, which is how h5storage writes every string."""
    handle[group].create_dataset(name, data=np.array([value.encode()]))


@pytest.fixture(name="simos")
def simos_fixture(tmp_path):
    """Build a simos_r0 file from the container shapes SIMO really writes.

    Named as no SIMO result file is, so the layout is read on its own; SIMO's
    two result files get SIMA's body handling on top, tested below.
    """
    h5py = pytest.importorskip("h5py")

    def build(builder, file: str = "sima_dynmod.h5") -> Path:
        run = tmp_path / "Task" / "Condition"
        run.mkdir(parents=True, exist_ok=True)
        with h5py.File(run / file, "w") as handle:
            handle.attrs["format"] = b"simos_r0"
            handle.attrs["order"] = b"results"
            builder(handle)
        return run

    return build


def _equally_spaced(handle, path="/results/bodies/0/force", name="XBRLF force",
                    unit="kN", values=(1.0, 2.0, 3.0), xstart=0.0, xdelta=0.5):
    handle.create_group(path)
    handle[path].attrs["type"] = b"marmo:containers:EquallySpacedSignal"
    handle[path].create_dataset("value", data=np.array(values, dtype=np.float64))
    handle[path].create_dataset("xstart", data=np.array([xstart]))
    handle[path].create_dataset("xdelta", data=np.array([xdelta]))
    _string(handle, path, "unit", unit)
    _string(handle, path, "xunit", "s")
    _string(handle, path, "name", name)


def test_an_equally_spaced_signal_is_rescaled_into_base_units(simos):
    run = simos(lambda h: _equally_spaced(h, unit="kN", values=(1.0, 2.0, 3.0)))

    res = open_results(run)
    signal = res["Condition/Dynamic/results/bodies/0/XBRLF force"]

    assert signal.unit == "N"
    assert signal.y.tolist() == [1000.0, 2000.0, 3000.0]
    assert signal.type == "marmo:containers:EquallySpacedSignal"


def test_the_axis_is_scaled_with_its_own_unit(simos):
    """xstart and xdelta are declared in the x unit, so they scale with it."""
    run = simos(lambda h: _equally_spaced(h, xstart=2.0, xdelta=0.5))

    signal = open_results(run)["Condition/Dynamic/results/bodies/0/XBRLF force"]

    assert signal.is_equidistant
    assert (signal.xstart, signal.xdelta) == (2.0, 0.5)
    assert signal.xunit == "s"


def test_a_signal_is_named_by_its_name_dataset(simos):
    """The HDF5 key is the DMT member name; the name dataset is what SIMA shows."""
    run = simos(lambda h: _equally_spaced(h, path="/results/x", name="Real Name"))

    assert open_results(run).signal("Condition/Dynamic/results/Real Name")


def test_a_container_is_named_by_its_name_dataset(simos):
    """findFolderName. Array members are keyed 0, 1, 2 -- without this every
    body reads as '0'."""

    def build(handle):
        _equally_spaced(handle, path="/results/bodies/0/force")
        _string(handle, "/results/bodies/0", "name", "FPSO")

    res = open_results(simos(build))

    assert res.signal("Condition/Dynamic/results/bodies/FPSO/XBRLF force")


def test_a_non_equally_spaced_signal_reads_both_axes(simos):
    def build(handle):
        path = "/results/line"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:NonEquallySpacedSignal"
        handle[path].create_dataset("value", data=np.array([1.0, 2.0]))
        handle[path].create_dataset("xvalue", data=np.array([10.0, 20.0]))
        _string(handle, path, "unit", "kN")
        _string(handle, path, "xunit", "m")
        _string(handle, path, "name", "T")
        _string(handle, path, "legend", "Tension at vertical level 29")
        _string(handle, path, "xlabel", "Horizontal distance")

    signal = open_results(simos(build))["Condition/Dynamic/results/T"]

    assert not signal.is_equidistant
    assert signal.x.tolist() == [10.0, 20.0]
    assert signal.y.tolist() == [1000.0, 2000.0]
    assert signal.unit == "N" and signal.xunit == "m"
    assert signal.attributes["legend"] == "Tension at vertical level 29"
    assert signal.attributes["xlabel"] == "Horizontal distance"


def test_a_dimensional_scalar_is_one_value(simos):
    def build(handle):
        path = "/results/depth"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:DimensionalScalar"
        handle[path].create_dataset("value", data=np.array([293.5]))
        _string(handle, path, "unit", "m")
        _string(handle, path, "name", "V")

    signal = open_results(simos(build))["Condition/Dynamic/results/V"]

    assert len(signal) == 1
    assert signal.y.tolist() == [293.5]
    assert signal.unit == "m"


def test_a_simple_string_is_read_as_text(simos):
    def build(handle):
        path = "/results/label"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:SimpleString"
        handle[path].create_dataset("value", data=np.array([b"some text"]))
        _string(handle, path, "name", "Comment")

    signal = open_results(simos(build))["Condition/Dynamic/results/Comment"]

    assert signal.y.tolist() == ["some text"]


def test_a_file_of_names_alone_yields_nothing(simos):
    """Real static results are often pure structure. Empty is not a failure."""
    def build(handle):
        handle.create_group("/results/bodies/0")
        _string(handle, "/results/bodies/0", "name", "FPSO")

    res = open_results(simos(build))

    assert not _signals(res)
    assert [s.status.value for s in res.sources] == ["read"]


def test_an_unknown_container_leaves_an_error_signal(simos):
    """Java raises and loses the file; a reader here is best effort."""
    def build(handle):
        _equally_spaced(handle, path="/results/good")
        handle.create_group("/results/odd")
        handle["/results/odd"].attrs["type"] = b"marmo:containers:SomethingNew"
        _string(handle, "/results/odd", "name", "Odd")

    signals = _signals(open_results(simos(build)))
    errors = [s for s in signals if isinstance(s, ErrorSignal)]

    assert len(signals) == 2, "the good signal survives the bad one"
    assert len(errors) == 1
    assert "SomethingNew" in str(errors[0].error)


def test_a_missing_required_name_leaves_an_error_signal(simos):
    """getRequiredString: absent or empty is a failure, not a default."""
    def build(handle):
        path = "/results/force"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:EquallySpacedSignal"
        handle[path].create_dataset("value", data=np.array([1.0]))
        _string(handle, path, "unit", "kN")
        _string(handle, path, "xunit", "s")

    signals = _signals(open_results(simos(build)))

    assert len(signals) == 1
    assert isinstance(signals[0], ErrorSignal)


def test_an_unknown_unit_is_tagged_and_warns_when_read(simos):
    """No unit engine here, so an unmapped label keeps the file's own numbers.

    Guessing a factor would be worse, but so would saying nothing: the values
    are not in the unit a caller would assume, so the signal is tagged and
    reading it warns.
    """
    run = simos(lambda h: _equally_spaced(h, unit="kip", values=(1.0,)))

    signal = open_results(run)["Condition/Dynamic/results/bodies/0/XBRLF force"]

    assert signal.unit == "kip"
    assert signal.attributes[UNSCALED_ATTRIBUTE] == "unit=kip"

    with pytest.warns(UserWarning, match="'kip' is not in SIMA's unit registry"):
        values = signal.y
    assert values.tolist() == [1.0], "the file's own numbers, not a guess"


def test_reading_a_tagged_signal_twice_warns_once(simos):
    """A loop over many signals should warn per signal, not per access."""
    run = simos(lambda h: _equally_spaced(h, unit="kip", values=(1.0,)))
    signal = open_results(run)["Condition/Dynamic/results/bodies/0/XBRLF force"]

    with pytest.warns(UserWarning):
        _ = signal.y
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        _ = signal.y  # no second warning, so this does not raise


def test_an_unknown_x_unit_warns_on_the_x_axis_only(simos):
    """Each axis is scaled by its own label, so each is judged separately."""
    def build(handle):
        path = "/results/line"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:NonEquallySpacedSignal"
        handle[path].create_dataset("value", data=np.array([1.0]))
        handle[path].create_dataset("xvalue", data=np.array([2.0]))
        _string(handle, path, "unit", "kN")
        _string(handle, path, "xunit", "furlong")
        _string(handle, path, "name", "T")

    signal = open_results(simos(build))["Condition/Dynamic/results/T"]

    assert signal.attributes[UNSCALED_ATTRIBUTE] == "xunit=furlong"
    with pytest.warns(UserWarning, match="xunit 'furlong'"):
        _ = signal.x
    # The y axis is in kN, which is known, so it is scaled and says nothing.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert signal.y.tolist() == [1000.0]


def test_a_known_unit_is_not_tagged_or_wrapped(simos):
    """The common case has to cost nothing."""
    run = simos(lambda h: _equally_spaced(h, unit="kN", values=(1.0,)))

    signal = open_results(run)["Condition/Dynamic/results/bodies/0/XBRLF force"]

    assert UNSCALED_ATTRIBUTE not in signal.attributes
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert signal.y.tolist() == [1000.0]


def test_loose_datasets_beside_the_groups_are_read(simos):
    """importAtomicData. These are unformatted-style, units in attributes."""
    def build(handle):
        _equally_spaced(handle, path="/results/bodies/0/force")
        loose = handle["/results/bodies/0"].create_dataset(
            "extra", data=np.array([1.0, 2.0])
        )
        loose.attrs["yunit"] = b"m"

    res = open_results(simos(build))

    assert res.signal("Condition/Dynamic/results/bodies/0/extra")


def test_a_variable_length_string_is_read_as_text(simos):
    h5py = pytest.importorskip("h5py")

    def build(handle):
        path = "/results/label"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:SimpleString"
        handle[path].create_dataset("value", data=["some text"], dtype=h5py.string_dtype())
        handle[path].create_dataset("name", data=["Comment"], dtype=h5py.string_dtype())

    signal = open_results(simos(build))["Condition/Dynamic/results/Comment"]

    assert signal.y.tolist() == ["some text"]


def test_an_empty_axis_dataset_fails_only_its_own_signal(simos):
    def build(handle):
        _equally_spaced(handle, path="/results/good", name="Good")
        _equally_spaced(handle, path="/results/bad", name="Bad")
        del handle["/results/bad/xdelta"]
        handle["/results/bad"].create_dataset("xdelta", data=np.array([]))

    res = open_results(simos(build))

    assert [s.status.value for s in res.sources] == ["read"]
    assert res.signal("Condition/Dynamic/results/Good").y.tolist() == [1000.0, 2000.0, 3000.0]
    assert isinstance(res.signal("Condition/Dynamic/results/bad"), ErrorSignal)


def test_an_x_row_of_another_length_falls_back_to_the_index(simos):
    def build(handle):
        path = "/results/line"
        handle.create_group(path)
        handle[path].attrs["type"] = b"marmo:containers:NonEquallySpacedSignal"
        handle[path].create_dataset("value", data=np.array([1.0, 2.0]))
        handle[path].create_dataset("xvalue", data=np.array([10.0, 20.0, 30.0]))
        _string(handle, path, "unit", "m")
        _string(handle, path, "xunit", "m")
        _string(handle, path, "name", "T")

    signal = open_results(simos(build))["Condition/Dynamic/results/T"]

    assert signal.x.tolist() == [0.0, 1.0]
    assert signal.y.tolist() == [1.0, 2.0]


# -- SIMO's own result files, as SIMOHDF5ResultsImporter reads them ---------


def _body(handle, index, name, signal=True):
    path = f"/results/bodies/{index}"
    if signal:
        _equally_spaced(handle, path=f"{path}/force")
    else:
        handle.create_group(path)
    _string(handle, path, "name", name)


@pytest.mark.parametrize("file", ["simo-dynamic-results.h5", "simo-static-results-sima.h5"])
def test_a_simo_result_file_puts_each_body_under_its_analysis(simos, file):
    def build(handle):
        _body(handle, 0, "Platform")
        _body(handle, 1, "Lifter")
        _string(handle, "/results/bodies", "name", "Bodies")

    run = simos(build, file)
    analysis = open_results(run).run.container("Static" if "static" in file else "Dynamic")

    assert [c.name for c in analysis.containers] == ["Platform", "Lifter"]
    platform = analysis.container("Platform")
    assert (platform.type, platform.attributes["body"]) == ("body", "Platform")
    assert platform.signal("XBRLF force").unit == "N"


def test_a_simo_result_file_keeps_other_containers_and_drops_loose_signals(simos):
    """As SIMA: only the containers below ``results`` are kept."""
    def build(handle):
        _body(handle, 0, "Platform")
        _equally_spaced(handle, path="/results/loose", name="Loose")
        handle.create_group("/results/extra")
        _equally_spaced(handle, path="/results/extra/0", name="Kept")

    dynamic = open_results(simos(build, "simo-dynamic-results.h5")).run.container("Dynamic")

    assert "Loose" not in dynamic
    assert "Platform" in dynamic

"""RIFLEX MatrixPlot files: the value pass, damaged files and matrix options."""

from pathlib import Path

import numpy as np
import pytest

from simapy.results import Container, ErrorSignal, Status, open_results
from simapy.results._readers import mpf
from simapy.results._sources import FolderContext, Source, SourceError

RUN = Path(__file__).parent / "data" / "Simple_Flexible_Riser" / "Initial"

ENVELOPE = "Initial/Dynamic/RiserLine/Displacement envelope curves"


def test_values_are_parsed_into_columns():
    signal = open_results(RUN).signal(f"{ENVELOPE}/X-MIN")

    assert signal.x[:2] == pytest.approx([0.0, 2.0])
    assert signal.y[:2] == pytest.approx([0.0, -2.3296811e-2])


def test_parsed_values_are_shared_and_read_only():
    signal = open_results(RUN).signal(f"{ENVELOPE}/X-MIN")

    assert np.shares_memory(signal.y, signal.y), "no copy per access"
    with pytest.raises(ValueError, match="read-only"):
        signal.y[0] = 1.0


def test_a_truncated_number_is_a_source_error_naming_the_line(copy_run):
    run = copy_run(RUN)
    content = (RUN / "sima_dynmod.mpf").read_bytes()
    cut = content.index(b"-3.2456455E-") + len(b"-3.2456455E-")
    (run / "sima_dynmod.mpf").write_bytes(content[:cut])
    line = content.count(b"\n", 0, cut) + 1

    signal = open_results(run).signal(f"{ENVELOPE}/X-MIN")

    with pytest.raises(SourceError, match=rf"sima_dynmod\.mpf, line {line}: .*-3\.2456455E-"):
        _ = signal.y


def test_a_matrix_cut_off_in_its_headers_keeps_the_ones_before_it(copy_run):
    run = copy_run(RUN)
    content = (RUN / "sima_dynmod.mpf").read_bytes()
    second = content.index(b"MATRIX    Displacement standard deviation")
    cut = content.index(b"\n", content.index(b"TITLE", second)) + 1
    (run / "sima_dynmod.mpf").write_bytes(content[:cut])

    res = open_results(run)

    assert [s.status for s in res.sources] == [Status.READ, Status.READ]
    assert res.signal(f"{ENVELOPE}/X-MIN").y[1] == pytest.approx(-2.3296811e-2)
    truncated = res.signal("Initial/Dynamic/RiserLine/Displacement standard deviation")
    assert isinstance(truncated, ErrorSignal)
    assert "truncated matrix" in str(truncated.error)


def test_switchxy_swaps_the_axes_and_their_units(tmp_path):
    path = _write(tmp_path / "curve.mpf", [
        "MATRIX    Curve",
        "TITLE     Curve",
        "XLABEL    Depth [m]",
        "YLABEL    Tension [kN]",
        "LEGENDS   'DEPTH' 'TENSION'",
        "OPTIONS   'SWITCHXY'",
        "VALUES     1.0E+000  2.0E+000",
        "           3.0E+000  4.0E+000",
        "END",
    ])

    signal = _read(path).signal("Curve/DEPTH")

    assert (signal.xunit, signal.unit) == ("N", "m")
    assert signal.x.tolist() == [2000.0, 4000.0]
    assert signal.y.tolist() == [1.0, 3.0]


def test_switchxy_on_more_than_two_series_fails_the_file(tmp_path):
    path = _write(tmp_path / "curve.mpf", [
        "MATRIX    Curve",
        "LEGENDS   'A' 'B' 'C'",
        "OPTIONS   'SWITCHXY'",
        "VALUES     1.0E+000  2.0E+000  3.0E+000",
        "END",
    ])

    with pytest.raises(SourceError, match="SWITCHXY should have two series"):
        _read(path)


def test_a_label_without_its_closing_bracket_keeps_its_unit(tmp_path):
    path = _write(tmp_path / "curve.mpf", [
        "MATRIX    Curve",
        "TITLE     Curve",
        "XLABEL    Line length [m",
        "YLABEL    Tension [kN",
        "LEGENDS   'S' 'T'",
        "VALUES     1.0E+000  2.0E+000",
        "END",
    ])

    signal = _read(path).signal("Curve/T")

    assert (signal.xunit, signal.unit) == ("m", "N")
    assert signal.y.tolist() == [2000.0]


def test_a_label_without_a_unit_still_resolves_short_ids():
    context = FolderContext(Path("."), names={"Risea63d": "RiserLine"})

    assert mpf._x_label("Length along Risea63d", context) == ("Length along RiserLine", "")


# -- helpers ---------------------------------------------------------------


def _write(path: Path, lines: list[str]) -> Path:
    path.write_bytes(("\n".join(lines) + "\n").encode(mpf.ENCODING))
    return path


def _read(path: Path) -> Container:
    container = Container("root")
    mpf.MpfReader().read(Source(path=path, context=FolderContext(path.parent)), container)
    return container

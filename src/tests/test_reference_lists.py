import pytest

from simapy.sima import riflex
from simapy.sima_reader import SIMAReader
from simapy.sima_writer import SIMAWriter


@pytest.mark.parametrize("extension", ["json", "h5"])
def test_a_list_of_references_round_trips(tmp_path, extension):
    """MassSummary.lines refers to lines contained elsewhere; dmtpy before 0.3.6 could not write it."""
    task = riflex.RIFLEXTask(name="task")
    task.model = riflex.RIFLEXModel()
    task.model.slenderSystem = riflex.SlenderSystem()
    lines = [riflex.ARLine(name="line1"), riflex.ARLine(name="line2")]
    task.model.slenderSystem.lines.extend(lines)
    summary = riflex.MassSummary(includeAllLines=False)
    summary.lines.extend(reversed(lines))
    task.model.riflexStaticCalculationParameters = riflex.RIFLEXStaticCalculationParameters(
        massSummary=summary)

    path = tmp_path / f"task.{extension}"
    SIMAWriter().write([task], str(path))
    read = SIMAReader().read(str(path))
    back = read[0] if isinstance(read, list) else read

    contained = back.model.slenderSystem.lines
    referenced = back.model.riflexStaticCalculationParameters.massSummary.lines
    assert [line.name for line in referenced] == ["line2", "line1"]
    assert all(r is c for r, c in zip(referenced, reversed(contained)))

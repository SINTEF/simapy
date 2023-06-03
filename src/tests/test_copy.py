from sima import simo


def test_different_copies():
    """Demonstrate how creating copies with and without external references works"""
    sys = simo.CatenarySystem()
    bp1 = simo.SIMOBodyPoint(name="bp1")
    bp2 = simo.SIMOBodyPoint(name="bp2")
    body = simo.SIMOBody(name="body")
    body.catenarySystem = sys
    body.bodyPoints = [bp1, bp2]
    line1 = simo.CatenaryLine(name="line1")
    line1.attachmentPoint = bp1
    line2 = simo.CatenaryLine(name="line2")
    line2.attachmentPoint = bp2
    sys.lines = [line1, line2]

    # First create a simple copy of the line without external references
    line1_copy = line1.copy(keep_uncontained_references=False)
    # Then the copy should not have an attachment point
    assert line1_copy.attachmentPoint is None

    # Make a copy with external references (the default)
    line1_copy = line1.copy(keep_uncontained_references=True)
    # Now the copy should retain the attachment point
    assert line1_copy.attachmentPoint is bp1

    body2 = body.copy()
    sys2 = body2.catenarySystem
    bp1_copy = body2.bodyPoints[0]
    bp2_copy = body2.bodyPoints[1]
    assert bp1_copy.name == "bp1"
    assert bp2_copy.name == "bp2"

    line1_copy = sys2.lines[0]
    assert line1_copy.name == "line1"
    assert line1_copy.attachmentPoint is bp1_copy

    line2_copy = sys2.lines[1]
    assert line2_copy.name == "line2"
    assert line2_copy.attachmentPoint is bp2_copy

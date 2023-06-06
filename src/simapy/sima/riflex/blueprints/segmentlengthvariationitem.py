# 
# Generated with SegmentLengthVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .segmentreference import SegmentReferenceBlueprint

class SegmentLengthVariationItemBlueprint(SegmentReferenceBlueprint):
    """"""

    def __init__(self, name="SegmentLengthVariationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("startTime","number","Start time for segment length variation",default=0.0))
        self.add_attribute(Attribute("endTime","number","End time for segment length variation",default=0.0))
        self.add_attribute(Attribute("segmentLengthRate","number","Segment length variation per time unit",default=0.0))
        self.add_attribute(Attribute("interactive","boolean","Activate interactive (HLA) control of segment variation",default=False))
# 
# Generated with ContactSurfacePointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .segmentreference import SegmentReferenceBlueprint

class ContactSurfacePointBlueprint(SegmentReferenceBlueprint):
    """"""

    def __init__(self, name="ContactSurfacePoint", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(EnumAttribute("segmentEnd","sima/riflex/End","Local segment end (1 or 2)."))
        self.add_attribute(BlueprintAttribute("tensioner","sima/riflex/Tensioner","Reference to tensioner contact type.",False))
        self.add_attribute(BlueprintAttribute("rollerContact","sima/riflex/RollerContact","Reference to roller contact type.",False))
        self.add_attribute(BlueprintAttribute("tubularContact","sima/riflex/TubularContact","Reference to tubular contact type.",False))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(EnumAttribute("segmentEnd","sima/riflex/End","Local segment end (1 or 2)."))
        self.attributes.append(BlueprintAttribute("tensioner","sima/riflex/Tensioner","Reference to tensioner contact type.",False))
        self.attributes.append(BlueprintAttribute("rollerContact","sima/riflex/RollerContact","Reference to roller contact type.",False))
        self.attributes.append(BlueprintAttribute("tubularContact","sima/riflex/TubularContact","Reference to tubular contact type.",False))
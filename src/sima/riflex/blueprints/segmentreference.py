# 
# Generated with SegmentReferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .linereference import LineReferenceBlueprint

class SegmentReferenceBlueprint(LineReferenceBlueprint):
    """"""

    def __init__(self, name="SegmentReference", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
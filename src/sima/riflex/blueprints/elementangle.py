# 
# Generated with ElementAngleBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .elementreference import ElementReferenceBlueprint

class ElementAngleBlueprint(ElementReferenceBlueprint):
    """"""

    def __init__(self, name="ElementAngle", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.add_attribute(Attribute("allElements","boolean","All elements",default=False))
        self.add_attribute(EnumAttribute("plane","sima/riflex/Plane","Angle with axis"))
        self.add_attribute(EnumAttribute("axis","sima/riflex/Axis","Projection in plane"))
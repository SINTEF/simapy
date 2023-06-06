# 
# Generated with MassSummaryBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class MassSummaryBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="MassSummary", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("calculateMassSummary","boolean","",default=False))
        self.add_attribute(EnumAttribute("reference","sima/riflex/MassSummaryReference","load step where this mass is calculated in static analysis"))
        self.add_attribute(Attribute("x","number","X coordinate",default=0.0))
        self.add_attribute(Attribute("y","number","Y coordinate",default=0.0))
        self.add_attribute(Attribute("z","number","Z coordinate",default=0.0))
        self.add_attribute(Attribute("rz","number","Rotation about z-axis",default=0.0))
        self.add_attribute(BlueprintAttribute("body","sima/simo/SIMOBody","",False))
        self.add_attribute(Attribute("includeAllLines","boolean","",default=True))
        self.add_attribute(BlueprintAttribute("lines","sima/riflex/ARLine","",False,Dimension("*")))
        self.add_attribute(EnumAttribute("loadStep","sima/riflex/MassSummaryStep","load step where this mass is calculated in static analysis"))
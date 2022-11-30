# 
# Generated with ForceResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ForceResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ForceResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string","Force name"))
        self.add_attribute(Attribute("fx","number","Statically calculated force",default=0.0))
        self.add_attribute(Attribute("fy","number","Statically calculated force",default=0.0))
        self.add_attribute(Attribute("fz","number","Statically calculated force",default=0.0))
        self.add_attribute(Attribute("mx","number","Statically calculated moment",default=0.0))
        self.add_attribute(Attribute("my","number","Statically calculated moment",default=0.0))
        self.add_attribute(Attribute("mz","number","Statically calculated moment",default=0.0))
        self.add_attribute(Attribute("mass","number","Mass of object",default=0.0))
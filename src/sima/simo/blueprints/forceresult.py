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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("fx","number","Statically calculated force",default=0.0))
        self.attributes.append(Attribute("fy","number","Statically calculated force",default=0.0))
        self.attributes.append(Attribute("fz","number","Statically calculated force",default=0.0))
        self.attributes.append(Attribute("mx","number","Statically calculated moment",default=0.0))
        self.attributes.append(Attribute("my","number","Statically calculated moment",default=0.0))
        self.attributes.append(Attribute("mz","number","Statically calculated moment",default=0.0))
        self.attributes.append(Attribute("mass","number","Mass of object",default=0.0))
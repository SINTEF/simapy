# 
# Generated with SoilItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SoilItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SoilItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("soilMaterial","sima/riflex/Soil","Soil material reference to valid material of type clay or sand",False))
        self.attributes.append(Attribute("lowerZ","number","The distance from mudline to lower end of soil layer",default=0.0))
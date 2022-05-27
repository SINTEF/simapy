# 
# Generated with AirFoilItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AirFoilItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AirFoilItem", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("angle","number","current angle-of-attack",default=0.0))
        self.attributes.append(Attribute("cl","number","Lift coefficient",default=0.0))
        self.attributes.append(Attribute("cd","number","Drag coefficient",default=0.0))
        self.attributes.append(Attribute("cm","number","Moment coefficient",default=0.0))
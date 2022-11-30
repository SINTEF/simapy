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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("angle","number","current angle-of-attack",default=0.0))
        self.add_attribute(Attribute("cl","number","Lift coefficient",default=0.0))
        self.add_attribute(Attribute("cd","number","Drag coefficient",default=0.0))
        self.add_attribute(Attribute("cm","number","Moment coefficient",default=0.0))
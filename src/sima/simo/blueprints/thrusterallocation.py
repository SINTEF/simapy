# 
# Generated with ThrusterAllocationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterAllocationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterAllocation", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("weight","number","Factor in weight function for thruster allocation",default=1.0))
        self.add_attribute(BlueprintAttribute("thruster","sima/simo/IThruster","Thruster controlled by the allocation system",False))
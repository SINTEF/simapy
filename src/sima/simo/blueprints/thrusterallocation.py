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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("weight","number","Factor in weight function for thruster allocation",default=1.0))
        self.attributes.append(BlueprintAttribute("thruster","sima/simo/IThruster","Thruster controlled by the allocation system",False))
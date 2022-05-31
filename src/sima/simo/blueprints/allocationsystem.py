# 
# Generated with AllocationSystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AllocationSystemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AllocationSystem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("surgeAllocation","boolean","Force allocation in surge",default=True))
        self.attributes.append(Attribute("swayAllocation","boolean","Force allocation in sway",default=True))
        self.attributes.append(Attribute("yawAllocation","boolean","Force allocation in yaw",default=True))
        self.attributes.append(BlueprintAttribute("thrusters","sima/simo/ThrusterAllocation","",True,Dimension("*")))
        self.attributes.append(Attribute("manual","boolean","Manual input of force to allocation system",default=False))
        self.attributes.append(EnumAttribute("allocationMethod","sima/simo/ThrusterAllocationMethod","Thrust allocation method"))
        self.attributes.append(BlueprintAttribute("thrusterControls","sima/simo/ThrusterControl","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("formulation","sima/simo/Formulation",""))
        self.attributes.append(Attribute("dpOff","boolean","Turn control system off",default=False))
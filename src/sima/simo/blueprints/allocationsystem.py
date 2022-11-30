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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("surgeAllocation","boolean","Force allocation in surge",default=True))
        self.add_attribute(Attribute("swayAllocation","boolean","Force allocation in sway",default=True))
        self.add_attribute(Attribute("yawAllocation","boolean","Force allocation in yaw",default=True))
        self.add_attribute(BlueprintAttribute("thrusters","sima/simo/ThrusterAllocation","",True,Dimension("*")))
        self.add_attribute(Attribute("manual","boolean","Manual input of force to allocation system",default=False))
        self.add_attribute(EnumAttribute("allocationMethod","sima/simo/ThrusterAllocationMethod","Thrust allocation method"))
        self.add_attribute(BlueprintAttribute("thrusterControls","sima/simo/ThrusterControl","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("formulation","sima/simo/Formulation",""))
        self.add_attribute(Attribute("dpOff","boolean","Turn control system off",default=False))
# 
# Generated with SupportVesselMotionScalingItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SupportVesselMotionScalingItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SupportVesselMotionScalingItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.add_attribute(Attribute("scalx","number","Scaling for global X-motion",default=1.0))
        self.add_attribute(Attribute("scaly","number","Scaling for global Y-motion",default=1.0))
        self.add_attribute(Attribute("scalz","number","Scaling for global Z-motion",default=1.0))
        self.add_attribute(Attribute("scalxr","number","Scaling for global X-rotation",default=1.0))
        self.add_attribute(Attribute("scalyr","number","Scaling for global Y-rotation",default=1.0))
        self.add_attribute(Attribute("scalzr","number","Scaling for global Z-rotation",default=1.0))
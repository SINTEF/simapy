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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.attributes.append(Attribute("scalx","number","Scaling for global X-motion",default=1.0))
        self.attributes.append(Attribute("scaly","number","Scaling for global Y-motion",default=1.0))
        self.attributes.append(Attribute("scalz","number","Scaling for global Z-motion",default=1.0))
        self.attributes.append(Attribute("scalxr","number","Scaling for global X-rotation",default=1.0))
        self.attributes.append(Attribute("scalyr","number","Scaling for global Y-rotation",default=1.0))
        self.attributes.append(Attribute("scalzr","number","Scaling for global Z-rotation",default=1.0))
# 
# Generated with OffsetVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class OffsetVariationItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="OffsetVariationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("referenceType","sima/riflex/ReferenceType","Reference to moving point"))
        self.add_attribute(Attribute("dx","number","Displacement increment, x-direction",default=0.0))
        self.add_attribute(Attribute("dy","number","Displacement increment, y-direction",default=0.0))
        self.add_attribute(Attribute("dz","number","Displacement increment, z-direction",default=0.0))
        self.add_attribute(EnumAttribute("rotationCode","sima/riflex/RotationCode","Rotation about axis"))
        self.add_attribute(Attribute("rotationIncrement","number","Rotation increments",default=0.0))
        self.add_attribute(BlueprintAttribute("supernode","sima/riflex/SuperNode","",False))
        self.add_attribute(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
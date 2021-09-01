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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("referenceType","sima/riflex/ReferenceType","Reference to moving point"))
        self.attributes.append(Attribute("dx","number","Displacement increment, x-direction",default=0.0))
        self.attributes.append(Attribute("dy","number","Displacement increment, y-direction",default=0.0))
        self.attributes.append(Attribute("dz","number","Displacement increment, z-direction",default=0.0))
        self.attributes.append(EnumAttribute("rotationCode","sima/riflex/RotationCode","Rotation about axis"))
        self.attributes.append(Attribute("rotationIncrement","number","Rotation increments",default=0.0))
        self.attributes.append(BlueprintAttribute("supernode","sima/riflex/SuperNode","",False))
        self.attributes.append(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
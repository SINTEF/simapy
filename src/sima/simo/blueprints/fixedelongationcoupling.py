# 
# Generated with FixedElongationCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simplecoupling import SimpleCouplingBlueprint

class FixedElongationCouplingBlueprint(SimpleCouplingBlueprint):
    """"""

    def __init__(self, name="FixedElongationCoupling", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.attributes.append(EnumAttribute("method","sima/simo/FixedElongationMethod","Method for initialisation of coupling element"))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.attributes.append(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
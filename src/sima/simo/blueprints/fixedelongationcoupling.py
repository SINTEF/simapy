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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.add_attribute(EnumAttribute("method","sima/simo/FixedElongationMethod","Method for initialisation of coupling element"))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.add_attribute(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
# 
# Generated with RatchetCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class RatchetCouplingBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="RatchetCoupling", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.add_attribute(EnumAttribute("_type","sima/simo/RatchetType","Ratchet type"))
        self.add_attribute(Attribute("staticForce","number","Static force in element",default=0.0))
        self.add_attribute(Attribute("stiffness","number","Element stiffness",default=0.0))
        self.add_attribute(Attribute("startTime","number","Time when dynamics in element will be activated",default=0.0))
        self.add_attribute(Attribute("dampingCoefficient","number","Damping coefficient",default=0.0))
        self.add_attribute(Attribute("exponent","number","Exponent in damping",default=0.0))
        self.add_attribute(Attribute("minVelocity","number","Velocity limit for damping force",default=0.0))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/FailureMode","Failure mode of coupling element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("maximumForce","number","Maximum force",default=0.0))
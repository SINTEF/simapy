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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("endPoint1","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(BlueprintAttribute("endPoint2","sima/simo/SIMOBodyPoint","",False))
        self.attributes.append(EnumAttribute("_type","sima/simo/RatchetType","Ratchet type"))
        self.attributes.append(Attribute("staticForce","number","Static force in element",default=0.0))
        self.attributes.append(Attribute("stiffness","number","Element stiffness",default=0.0))
        self.attributes.append(Attribute("startTime","number","Time when dynamics in element will be activated",default=0.0))
        self.attributes.append(Attribute("dampingCoefficient","number","Damping coefficient",default=0.0))
        self.attributes.append(Attribute("exponent","number","Exponent in damping",default=0.0))
        self.attributes.append(Attribute("minVelocity","number","Velocity limit for damping force",default=0.0))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/FailureMode","Failure mode of coupling element"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("maximumForce","number","Maximum force",default=0.0))
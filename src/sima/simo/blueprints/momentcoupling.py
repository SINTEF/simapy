# 
# Generated with MomentCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class MomentCouplingBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="MomentCoupling", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("body1","sima/simo/SIMOBody","",False))
        self.add_attribute(BlueprintAttribute("rotationVector","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("body2","sima/simo/SIMOBody","",False))
        self.add_attribute(Attribute("initialMoment","number","Initial moment",default=0.0))
        self.add_attribute(Attribute("stiffness","number","Moment stiffness",default=0.0))
        self.add_attribute(Attribute("positiveDamping","number","Damping coefficient for positive rotation",default=0.0))
        self.add_attribute(Attribute("positiveExponent","number","Exponent in damping for positive rotation",default=0.0))
        self.add_attribute(Attribute("negativeDamping","number","Damping coefficient for negative rotation",default=0.0))
        self.add_attribute(Attribute("negativeExponent","number","Exponent in damping for negative rotation",default=0.0))
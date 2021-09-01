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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("body1","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("rotationVector","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("body2","sima/simo/SIMOBody","",False))
        self.attributes.append(Attribute("initialMoment","number","Initial moment",default=0.0))
        self.attributes.append(Attribute("stiffness","number","Moment stiffness",default=0.0))
        self.attributes.append(Attribute("positiveDamping","number","Damping coefficient for positive rotation",default=0.0))
        self.attributes.append(Attribute("positiveExponent","number","Exponent in damping for positive rotation",default=0.0))
        self.attributes.append(Attribute("negativeDamping","number","Damping coefficient for negative rotation",default=0.0))
        self.attributes.append(Attribute("negativeExponent","number","Exponent in damping for negative rotation",default=0.0))
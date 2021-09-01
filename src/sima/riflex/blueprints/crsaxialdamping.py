# 
# Generated with CRSAxialDampingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CRSAxialDampingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CRSAxialDamping", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("constantDamping","boolean","Damping coefficient code",default=False))
        self.attributes.append(Attribute("strainVelocityExponent","number","Exponent for strain velocity",default=1.0))
        self.attributes.append(Attribute("dampingCoefficient","number","Damping coefficient (constant)",default=0.0))
        self.attributes.append(BlueprintAttribute("dampingCoefficientCharacteristics","sima/riflex/CRSAxialDampingItem","",True,Dimension("size","")))
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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("constantDamping","boolean","Damping coefficient code",default=False))
        self.add_attribute(Attribute("strainVelocityExponent","number","Exponent for strain velocity",default=1.0))
        self.add_attribute(Attribute("dampingCoefficient","number","Damping coefficient (constant)",default=0.0))
        self.add_attribute(BlueprintAttribute("dampingCoefficientCharacteristics","sima/riflex/CRSAxialDampingItem","",True,Dimension("*")))
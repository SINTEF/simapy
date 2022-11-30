# 
# Generated with ClayBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .soil import SoilBlueprint

class ClayBlueprint(SoilBlueprint):
    """"""

    def __init__(self, name="Clay", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("strainVelocityExponent","number","Strain velocity exponent for damping model",default=1.0))
        self.add_attribute(Attribute("calculateDamping","boolean","Calculate damping coefficients",default=False))
        self.add_attribute(BlueprintAttribute("dampingItems","sima/riflex/SoilDampingItem","",True,Dimension("*")))
        self.add_attribute(Attribute("upperWeight","number","",default=0.0))
        self.add_attribute(Attribute("lowerWeight","number","",default=0.0))
        self.add_attribute(Attribute("displacement","number","Target displacement for generating equivalent damping coefficient",default=0.0))
        self.add_attribute(Attribute("frequency","number","Target frequency for generating equivalent damping coefficient",default=0.0))
        self.add_attribute(Attribute("initialShearModulus","number","Initial shear modulus of soil",default=0.0))
        self.add_attribute(Attribute("upperShearStrength","number","Undrained shear strength",default=0.0))
        self.add_attribute(Attribute("upperJConstant","number","Dimensionless constant",default=0.0))
        self.add_attribute(Attribute("upperStrain","number","Strain at one-half the maximum stress in undrained compression",default=0.0))
        self.add_attribute(Attribute("lowerShearStrength","number","Undrained shear strength",default=0.0))
        self.add_attribute(Attribute("lowerJConstant","number","Dimensionless constant",default=0.0))
        self.add_attribute(Attribute("lowerStrain","number","Strain at one-half the maximum stress in undrained compression",default=0.0))
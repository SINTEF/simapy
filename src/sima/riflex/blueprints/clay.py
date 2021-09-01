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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("strainVelocityExponent","number","Strain velocity exponent for damping model",default=1.0))
        self.attributes.append(Attribute("calculateDamping","boolean","Calculate damping coefficients",default=False))
        self.attributes.append(BlueprintAttribute("dampingItems","sima/riflex/SoilDampingItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("upperWeight","number","",default=0.0))
        self.attributes.append(Attribute("lowerWeight","number","",default=0.0))
        self.attributes.append(Attribute("displacement","number","Target displacement for generating equivalent damping coefficient",default=0.0))
        self.attributes.append(Attribute("frequency","number","Target frequency for generating equivalent damping coefficient",default=0.0))
        self.attributes.append(Attribute("initialShearModulus","number","Initial shear modulus of soil",default=0.0))
        self.attributes.append(Attribute("upperShearStrength","number","Undrained shear strength",default=0.0))
        self.attributes.append(Attribute("upperJConstant","number","Dimensionless constant",default=0.0))
        self.attributes.append(Attribute("upperStrain","number","Strain at one-half the maximum stress in undrained compression",default=0.0))
        self.attributes.append(Attribute("lowerShearStrength","number","Undrained shear strength",default=0.0))
        self.attributes.append(Attribute("lowerJConstant","number","Dimensionless constant",default=0.0))
        self.attributes.append(Attribute("lowerStrain","number","Strain at one-half the maximum stress in undrained compression",default=0.0))
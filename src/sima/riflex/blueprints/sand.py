# 
# Generated with SandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .soil import SoilBlueprint

class SandBlueprint(SoilBlueprint):
    """"""

    def __init__(self, name="Sand", package_path="sima/riflex", description=""):
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
        self.add_attribute(Attribute("upperFrictionAngle","number","Angle of internal friction of sand",default=0.0))
        self.add_attribute(Attribute("lowerFrictionAngle","number","Angle of internal friction of sand",default=0.0))
        self.add_attribute(Attribute("angleOfSoilFriction","number","Angle of soil friction on pile wall",default=15.0))
        self.add_attribute(Attribute("limitingSkinFriction","number","Limiting unit skin friction",default=48000.0))
        self.add_attribute(Attribute("bearingFactor","number","Bearing factor",default=8.0))
        self.add_attribute(Attribute("limitingTipResistance","number","Limiting tip resistance",default=1900000.0))
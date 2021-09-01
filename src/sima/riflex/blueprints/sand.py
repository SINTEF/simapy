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
        self.attributes.append(Attribute("upperFrictionAngle","number","Angle of internal friction of sand",default=0.0))
        self.attributes.append(Attribute("lowerFrictionAngle","number","Angle of internal friction of sand",default=0.0))
        self.attributes.append(Attribute("angleOfSoilFriction","number","Angle of soil friction on pile wall",default=15.0))
        self.attributes.append(Attribute("limitingSkinFriction","number","Limiting unit skin friction",default=48000.0))
        self.attributes.append(Attribute("bearingFactor","number","Bearing factor",default=8.0))
        self.attributes.append(Attribute("limitingTipResistance","number","Limiting tip resistance",default=1900000.0))
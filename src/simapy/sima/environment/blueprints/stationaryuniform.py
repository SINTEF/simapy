# 
# Generated with StationaryUniformBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class StationaryUniformBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="StationaryUniform", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("horizontalVelocity","number","Horizontal wind velocity component",default=0.0))
        self.add_attribute(Attribute("verticalVelocity","number","Vertical wind velocity component",default=0.0))
        self.add_attribute(BlueprintAttribute("velocityProfiles","sima/environment/ShearWindVelocityProfile","",True,Dimension("*")))
        self.add_attribute(Attribute("lowerEdgeZ","number","Z coordinate of the lower edge of the wind field domain",default=0.0))
        self.add_attribute(Attribute("domainResolution","number","Domain resolution in Z- (vertical) direction",default=0.0))
        self.add_attribute(Attribute("numGridPoints","integer","Number of grid points in Z- (vertical) direction",default=0))
        self.add_attribute(EnumAttribute("shearProfile","sima/environment/ShearProfile",""))
        self.add_attribute(Attribute("referenceHeight","number","Reference height for which the horizontal and vertical wind velocity values are given.",default=0.0))
        self.add_attribute(Attribute("windShearExponent","number","Exponent in the power shear profile",default=0.0))
        self.add_attribute(Attribute("roughnessLength","number","",default=0.0))
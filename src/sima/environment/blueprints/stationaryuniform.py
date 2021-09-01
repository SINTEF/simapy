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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.attributes.append(Attribute("horizontalVelocity","number","Horizontal wind velocity component",default=0.0))
        self.attributes.append(Attribute("verticalVelocity","number","Vertical wind velocity component",default=0.0))
        self.attributes.append(BlueprintAttribute("velocityProfiles","sima/environment/ShearWindVelocityProfile","",True,Dimension("size","")))
        self.attributes.append(Attribute("lowerEdgeZ","number","Z coordinate of the lower edge of the wind field domain",default=0.0))
        self.attributes.append(Attribute("domainResolution","number","Domain resolution in Z- (vertical) direction",default=0.0))
        self.attributes.append(Attribute("numGridPoints","integer","Number of grid points in Z- (vertical) direction",default=0))
        self.attributes.append(EnumAttribute("shearProfile","sima/environment/ShearProfile",""))
        self.attributes.append(Attribute("referenceHeight","number","Reference height for which the horizontal and vertical wind velocity values are given.",default=0.0))
        self.attributes.append(Attribute("windShearExponent","number","Exponent in the power shear profile",default=0.0))
        self.attributes.append(Attribute("roughnessLength","number","",default=0.0))
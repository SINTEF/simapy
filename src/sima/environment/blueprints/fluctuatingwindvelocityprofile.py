# 
# Generated with FluctuatingWindVelocityProfileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .windvelocityprofile import WindVelocityProfileBlueprint

class FluctuatingWindVelocityProfileBlueprint(WindVelocityProfileBlueprint):
    """"""

    def __init__(self, name="FluctuatingWindVelocityProfile", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("verticalCoordinate","number","Vertical coordinate of profile level",default=0.0))
        self.attributes.append(Attribute("longitudinalVelocityFactor","number","Wind speed scaling factor for fluctuating part of the longitudinal wind",default=0.0))
        self.attributes.append(Attribute("lateralVelocityFactor","number","Wind speed scaling factor for the lateral wind velocity",default=0.0))
        self.attributes.append(Attribute("verticalVelocityFactor","number","Wind speed scaling factor for the vertical wind velocity",default=0.0))
        self.attributes.append(Attribute("meanSpeedFactor","number","Wind speed scaling factor for the mean wind speed",default=0.0))
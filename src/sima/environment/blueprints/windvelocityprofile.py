# 
# Generated with WindVelocityProfileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WindVelocityProfileBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WindVelocityProfile", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("verticalCoordinate","number","Vertical coordinate of profile level",default=0.0))
        self.attributes.append(Attribute("longitudinalVelocityFactor","number","Wind speed scaling factor for fluctuating part of the longitudinal wind",default=0.0))
        self.attributes.append(Attribute("lateralVelocityFactor","number","Wind speed scaling factor for the lateral wind velocity",default=0.0))
        self.attributes.append(Attribute("verticalVelocityFactor","number","Wind speed scaling factor for the vertical wind velocity",default=0.0))
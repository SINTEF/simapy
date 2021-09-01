# 
# Generated with ShearWindVelocityProfileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ShearWindVelocityProfileBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ShearWindVelocityProfile", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("verticalCoordinate","number","Vertical coordinate of profile level",default=0.0))
        self.attributes.append(Attribute("horizontalVelocityFactor","number","Wind speed scaling factor for fluctuating part of the horizontal wind",default=0.0))
        self.attributes.append(Attribute("verticalVelocityFactor","number","Wind speed scaling factor for the vertical wind velocity",default=0.0))
        self.attributes.append(Attribute("direction","number","",default=0.0))
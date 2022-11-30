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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("verticalCoordinate","number","Vertical coordinate of profile level",default=0.0))
        self.add_attribute(Attribute("horizontalVelocityFactor","number","Wind speed scaling factor for fluctuating part of the horizontal wind",default=0.0))
        self.add_attribute(Attribute("verticalVelocityFactor","number","Wind speed scaling factor for the vertical wind velocity",default=0.0))
        self.add_attribute(Attribute("direction","number","",default=0.0))
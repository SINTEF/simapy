# 
# Generated with GuidanceSystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class GuidanceSystemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GuidanceSystem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("guidance","sima/simo/Guidance",""))
        self.add_attribute(EnumAttribute("waypointReference","sima/simo/WaypointReference",""))
        self.add_attribute(EnumAttribute("headingReference","sima/simo/HeadingReference",""))
        self.add_attribute(Attribute("startTime","number","Start time for guidance system",default=200.0))
        self.add_attribute(Attribute("maxAccelerationX","number","Max. acceleration in local x-direction",default=0.0))
        self.add_attribute(Attribute("maxAccelerationY","number","Max. acceleration in local y-direction",default=0.0))
        self.add_attribute(BlueprintAttribute("waypoints","sima/simo/Waypoint","",True,Dimension("*")))
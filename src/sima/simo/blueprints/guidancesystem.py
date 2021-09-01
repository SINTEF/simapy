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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("guidance","sima/simo/Guidance",""))
        self.attributes.append(EnumAttribute("waypointReference","sima/simo/WaypointReference",""))
        self.attributes.append(EnumAttribute("headingReference","sima/simo/HeadingReference",""))
        self.attributes.append(Attribute("startTime","number","Start time for guidance system",default=200.0))
        self.attributes.append(Attribute("maxAccelerationX","number","Max. acceleration in local x-direction",default=0.0))
        self.attributes.append(Attribute("maxAccelerationY","number","Max. acceleration in local y-direction",default=0.0))
        self.attributes.append(BlueprintAttribute("waypoints","sima/simo/Waypoint","",True,Dimension("size","")))
# 
# Generated with WaypointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WaypointBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Waypoint", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("x","number","X-coordinate of waypoint",default=0.0))
        self.attributes.append(Attribute("y","number","Y-coordinate of waypoint",default=0.0))
        self.attributes.append(Attribute("velocity","number","Velocity towards next waypoint",default=0.0))
        self.attributes.append(Attribute("heading","number","Heading towards next waypoint (Only for fixed heading reference)",default=0.0))
        self.attributes.append(Attribute("turningRadius","number","Turning radius of waypoint ( Maximum rate of turn = velocity/turning radius)",default=0.0))
        self.attributes.append(Attribute("radiusOfAcceptance","number","Radius of acceptance ( Select next waypoint when within radius of acceptance )",default=0.0))
        self.attributes.append(Attribute("lineOfSight","number","Line of sight length (Determines the line from the vessel to the intersection of the line between the current waypoint and the next)",default=0.0))
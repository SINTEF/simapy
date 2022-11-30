# 
# Generated with ThrusterControlBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterControlBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterControl", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("thruster","sima/simo/IThruster","Thruster to be controlled",False))
        self.add_attribute(EnumAttribute("thrusterControlType","sima/simo/DPThrusterType","Thruster control type"))
        self.add_attribute(Attribute("direction","number","Direction of thruster. Start value for azimuthing thrusters.",default=0.0))
        self.add_attribute(Attribute("minForce","number","Minimum force",default=0.0))
        self.add_attribute(Attribute("maxForce","number","Maximum force",default=0.0))
        self.add_attribute(Attribute("maxForceRate","number","Maximum rate of force",default=0.0))
        self.add_attribute(Attribute("maxAngleRate","number","Maximum rate of azimuth angle",default=0.0))
        self.add_attribute(Attribute("x","number","X-coordinate of thruster in body system",default=0.0))
        self.add_attribute(Attribute("y","number","Y-coordinate of thruster in body system",default=0.0))
        self.add_attribute(Attribute("z","number","Z-coordinate of thruster in body system",default=0.0))
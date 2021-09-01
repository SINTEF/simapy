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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("thruster","sima/simo/IThruster","Thruster to be controlled",False))
        self.attributes.append(EnumAttribute("thrusterControlType","sima/simo/DPThrusterType","Thruster control type"))
        self.attributes.append(Attribute("direction","number","Direction of thruster. Start value for azimuthing thrusters.",default=0.0))
        self.attributes.append(Attribute("minForce","number","Minimum force",default=0.0))
        self.attributes.append(Attribute("maxForce","number","Maximum force",default=0.0))
        self.attributes.append(Attribute("maxForceRate","number","Maximum rate of force",default=0.0))
        self.attributes.append(Attribute("maxAngleRate","number","Maximum rate of azimuth angle",default=0.0))
        self.attributes.append(Attribute("x","number","X-coordinate of thruster in body system",default=0.0))
        self.attributes.append(Attribute("y","number","Y-coordinate of thruster in body system",default=0.0))
        self.attributes.append(Attribute("z","number","Z-coordinate of thruster in body system",default=0.0))
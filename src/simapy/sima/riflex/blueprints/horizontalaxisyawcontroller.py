# 
# Generated with HorizontalAxisYawControllerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...windturbine.blueprints.yawcontroller import YawControllerBlueprint

class HorizontalAxisYawControllerBlueprint(YawControllerBlueprint):
    """"""

    def __init__(self, name="HorizontalAxisYawController", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("yawControllerType","sima/windturbine/YawControllerType",""))
        self.add_attribute(Attribute("timeStep","number","",default=0.0))
        self.add_attribute(Attribute("setPoint","number","Desired yaw misalignment",default=0.0))
        self.add_attribute(Attribute("yawRate","number","",default=0.0))
        self.add_attribute(Attribute("errorThreshold","number","Yaw misalignment integrated error threshold",default=0.0))
        self.add_attribute(Attribute("fastLowPassFilterPeriod","number","Filter period for yaw misalignment signal. Used for determining if 'error threshold' has been passed",default=0.0))
        self.add_attribute(Attribute("slowLowPassFilterPeriod","number","Filter period for yaw misalignment signal. Used to determine end time for yawing back to set point",default=0.0))
        self.add_attribute(BlueprintAttribute("referenceLine","sima/riflex/ARLine","Line where end 2 is the fixed reference for the applied yaw angle",False))
        self.add_attribute(BlueprintAttribute("yawLine","sima/riflex/ARLine","Line where yaw angle is applied in end 1",False))
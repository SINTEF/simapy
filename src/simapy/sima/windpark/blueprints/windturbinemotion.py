# 
# Generated with WindTurbineMotionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class WindTurbineMotionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WindTurbineMotion", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("turbine","sima/windpark/WindParkTurbine","",False))
        self.add_attribute(Attribute("timeColumn","integer","Column number for time",default=0))
        self.add_attribute(Attribute("shaftDirectionColumn","integer","Column or time series number for shaft direction",default=0))
        self.add_attribute(EnumAttribute("motionType","sima/windpark/MotionType","Kind of motion time series input"))
        self.add_attribute(Attribute("file","string","File name for hub positions"))
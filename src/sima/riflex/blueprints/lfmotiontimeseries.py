# 
# Generated with LFMotionTimeSeriesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LFMotionTimeSeriesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LFMotionTimeSeries", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("timeSeriesFile","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.add_attribute(Attribute("fileName","string","Motion time series file"))
        self.add_attribute(EnumAttribute("fileFormat","sima/riflex/FileFormatAsciStarNone","Motion time series file format"))
        self.add_attribute(EnumAttribute("motionTimeSeriesType","sima/riflex/MotionTimeSeriesType","Kind of motion time series input"))
        self.add_attribute(EnumAttribute("rotationUnit","sima/riflex/RotationUnit","Rotation unit"))
        self.add_attribute(Attribute("timeColumnNum","integer","Column number for time (Does not apply to STAR files)",default=1))
        self.add_attribute(Attribute("xMotionColumn","integer","Column or time series number for global dynamic x-motion",default=0))
        self.add_attribute(Attribute("xMotionVersion","integer","Startimes version number for global dynamic x-motion",default=0))
        self.add_attribute(Attribute("yMotionColumn","integer","Column or time series number for global dynamic y-motion",default=0))
        self.add_attribute(Attribute("yMotionVersion","integer","Startimes version number for global dynamic y-motion",default=0))
        self.add_attribute(Attribute("zRotationColumn","integer","Column or time series number for global dynamic z-rotation",default=0))
        self.add_attribute(Attribute("zRotationVersion","integer","Startimes version number for global dynamic z-rotation",default=0))
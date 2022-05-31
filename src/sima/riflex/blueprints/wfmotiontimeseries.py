# 
# Generated with WFMotionTimeSeriesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WFMotionTimeSeriesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WFMotionTimeSeries", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("timeSeriesFile","boolean","",default=False))
        self.attributes.append(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.attributes.append(Attribute("fileName","string","Motion time series file",default=""))
        self.attributes.append(EnumAttribute("fileFormat","sima/riflex/FileFormatAsciStarNone","Motion time series file format"))
        self.attributes.append(EnumAttribute("motionTimeSeriesType","sima/riflex/MotionTimeSeriesType","Kind of motion time series input"))
        self.attributes.append(EnumAttribute("rotationUnit","sima/riflex/RotationUnit","Rotation unit"))
        self.attributes.append(Attribute("timeColumnNum","integer","Column number for time (Does not apply to STAR files)",default=1))
        self.attributes.append(Attribute("xMotionColumn","integer","Column or time series number for global dynamic x-motion",default=0))
        self.attributes.append(Attribute("xMotionVersion","integer","Startimes version number for global dynamic x-motion",default=0))
        self.attributes.append(Attribute("yMotionColumn","integer","Column or time series number for global dynamic y-motion",default=0))
        self.attributes.append(Attribute("yMotionVersion","integer","Startimes version number for global dynamic y-motion",default=0))
        self.attributes.append(Attribute("zRotationColumn","integer","Column or time series number for global dynamic z-rotation",default=0))
        self.attributes.append(Attribute("zRotationVersion","integer","Startimes version number for global dynamic z-rotation",default=0))
        self.attributes.append(Attribute("zMotionColumn","integer","Column or time series number for global dynamic z-motion",default=0))
        self.attributes.append(Attribute("zMotionVersion","integer","Startimes version number for global dynamic z-motion",default=0))
        self.attributes.append(Attribute("xRotationColumn","integer","Column or time series number for global dynamic x-rotation",default=0))
        self.attributes.append(Attribute("xRotationVersion","integer","Startimes version number for global dynamic x-rotation",default=0))
        self.attributes.append(Attribute("yRotationColumn","integer","Column or time series number for global dynamic y-rotation",default=0))
        self.attributes.append(Attribute("yRotationVersion","integer","Startimes version number for global dynamic y-rotation",default=0))
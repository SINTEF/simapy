# 
# Generated with WaveTimeSeriesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WaveTimeSeriesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WaveTimeSeries", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("fileName","string","Wave time series file",default=""))
        self.attributes.append(EnumAttribute("fileFormat","sima/riflex/FileFormatAsciStar","Wave time series file format"))
        self.attributes.append(Attribute("timeColumnNum","integer","Column number for time",default=1))
        self.attributes.append(Attribute("waveColumnNum","integer","Column or time series number for wave elevation",default=2))
        self.attributes.append(Attribute("starFileVersion","integer","Startimes file version",default=0))
        self.attributes.append(Attribute("direction","number","Wave direction",default=0.0))
        self.attributes.append(Attribute("xgWav","number","Global x-coordinate for position where time series is measured",default=0.0))
        self.attributes.append(Attribute("ygWav","number","Global y-coordinate for position where time series is measured",default=0.0))
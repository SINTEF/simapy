# 
# Generated with DoubleModelSpectrumBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wave import WaveBlueprint

class DoubleModelSpectrumBlueprint(WaveBlueprint):
    """"""

    def __init__(self, name="DoubleModelSpectrum", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("significantWaveHeight","number","Significant wave height",default=0.0))
        self.attributes.append(Attribute("windDrivenRatio","number","Ratio of wind driven sea to the total sea.",default=0.0))
        self.attributes.append(Attribute("windPeakPeriod","number","Peak period of the wind driven sea",default=0.0))
        self.attributes.append(Attribute("swellPeakPeriod","number","Peak period of the swell sea",default=0.0))
        self.attributes.append(Attribute("gammaWind","number","Gamma parameter for wind driven sea",default=3.3))
        self.attributes.append(Attribute("gammaSwell","number","Gamma parameter for swell sea",default=0.0))
        self.attributes.append(Attribute("upperSlopeWind","number","Slope of the upper frequency part of the wind driven part of wave spectrum",default=0.0))
        self.attributes.append(Attribute("lowerSlopeWind","number","Slope of the lower frequency part of the wind driven part of wave spectrum",default=0.0))
        self.attributes.append(Attribute("upperSlopeSwell","number","Slope of the upper frequency part of the swell part of wave spectrum",default=0.0))
        self.attributes.append(Attribute("lowerSlopeSwell","number","Slope of the lower frequency part of the swell part of wave spectrum",default=0.0))
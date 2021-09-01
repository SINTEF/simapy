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

    def __init__(self, name="WaveTimeSeries", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("scaleFactor","number","Wave scale factor",default=1.0))
        self.attributes.append(Attribute("refPointX","number","Reference point X",default=0.0))
        self.attributes.append(Attribute("refPointY","number","Reference point Y",default=0.0))
        self.attributes.append(Attribute("waterDepth","number","Water depth in FULL scale",default=0.0))
        self.attributes.append(Attribute("fileName","string","",default=""))
        self.attributes.append(Attribute("filterInputTimeseries","boolean","Apply filtering to the wave signal",default=True))
        self.attributes.append(Attribute("specifyLowerPeriod","boolean","Override default computation of lower cut off period",default=True))
        self.attributes.append(Attribute("lowerCutOffPeriod","number","Lower cut off period for filtering of wave signal",default=0.0))
        self.attributes.append(Attribute("upperCutOffPeriod","number","Upper cut off period for filtering of wave signal",default=40.0))
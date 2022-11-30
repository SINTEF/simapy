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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("scaleFactor","number","Wave scale factor",default=1.0))
        self.add_attribute(Attribute("refPointX","number","Reference point X",default=0.0))
        self.add_attribute(Attribute("refPointY","number","Reference point Y",default=0.0))
        self.add_attribute(Attribute("waterDepth","number","Water depth in FULL scale",default=0.0))
        self.add_attribute(Attribute("fileName","string",""))
        self.add_attribute(Attribute("filterInputTimeseries","boolean","Apply filtering to the wave signal",default=True))
        self.add_attribute(Attribute("specifyLowerPeriod","boolean","Override default computation of lower cut off period",default=False))
        self.add_attribute(Attribute("lowerCutOffPeriod","number","Lower cut off period for filtering of wave signal",default=0.0))
        self.add_attribute(Attribute("upperCutOffPeriod","number","Upper cut off period for filtering of wave signal",default=40.0))
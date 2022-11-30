# 
# Generated with LongTermStatisticsWaveCalculationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LongTermStatisticsWaveCalculationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LongTermStatisticsWaveCalculation", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("returnPeriod","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("statistics","sima/metocean/WaveLongTermStatistics","",False))
        self.add_attribute(BlueprintAttribute("omni","sima/metocean/OmniDirectionalWaveLongTermStatistics","",False))
        self.add_attribute(EnumAttribute("method","sima/metocean/WaveStatisticsMethod",""))
        self.add_attribute(BlueprintAttribute("directions","sima/metocean/CalculationDirection","",True,Dimension("*")))
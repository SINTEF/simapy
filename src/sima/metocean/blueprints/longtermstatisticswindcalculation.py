# 
# Generated with LongTermStatisticsWindCalculationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LongTermStatisticsWindCalculationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LongTermStatisticsWindCalculation", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("returnPeriod","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("levels","sima/metocean/CalculationLevel","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("method","sima/metocean/LevelStatisticsMethod",""))
        self.add_attribute(EnumAttribute("omniMethod","sima/metocean/LevelStatisticsMethod",""))
        self.add_attribute(Attribute("directionRelativeToWave","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("statistics","sima/metocean/WindLongTermStatistics","",False))
        self.add_attribute(BlueprintAttribute("omni","sima/metocean/WindLongTermStatistics","",False))
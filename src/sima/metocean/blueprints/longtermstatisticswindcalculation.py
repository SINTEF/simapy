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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("returnPeriod","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("levels","sima/metocean/CalculationLevel","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("method","sima/metocean/LevelStatisticsMethod",""))
        self.attributes.append(EnumAttribute("omniMethod","sima/metocean/LevelStatisticsMethod",""))
        self.attributes.append(Attribute("directionRelativeToWave","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("statistics","sima/metocean/WindLongTermStatistics","",False))
        self.attributes.append(BlueprintAttribute("omni","sima/metocean/WindLongTermStatistics","",False))
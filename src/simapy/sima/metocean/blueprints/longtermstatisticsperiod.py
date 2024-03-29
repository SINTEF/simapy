# 
# Generated with LongTermStatisticsPeriodBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.named import NamedBlueprint

class LongTermStatisticsPeriodBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="LongTermStatisticsPeriod", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("waveStatistics","sima/metocean/WaveLongTermStatistics","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("windStatistics","sima/metocean/WindLongTermStatistics","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("currentStatistics","sima/metocean/CurrentLongTermStatistics","",True,Dimension("*")))
# 
# Generated with WindLongTermStatisticsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class WindLongTermStatisticsBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="WindLongTermStatistics", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("weibullDistributions","sima/metocean/WeibullDistribution","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("extremes","sima/metocean/LevelExtreme","",True,Dimension("*")))
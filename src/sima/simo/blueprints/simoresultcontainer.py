# 
# Generated with SIMOResultContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.conditionresultcontainer import ConditionResultContainerBlueprint

class SIMOResultContainerBlueprint(ConditionResultContainerBlueprint):
    """"""

    def __init__(self, name="SIMOResultContainer", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(Attribute("modelOutputFile","string",""))
        self.add_attribute(Attribute("probability","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("static","sima/simo/SIMOStaticResultEntry","",True))
        self.add_attribute(BlueprintAttribute("dynamic","sima/simo/SIMODynamicResultEntry","",True))
        self.add_attribute(BlueprintAttribute("stability","sima/sima/ResultEntry","",True))
        self.add_attribute(BlueprintAttribute("preRunResults","sima/sima/ResultEntry","",True))
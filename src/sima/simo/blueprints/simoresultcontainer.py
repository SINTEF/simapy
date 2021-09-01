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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("size","")))
        self.attributes.append(Attribute("modelOutputFile","string","",default=""))
        self.attributes.append(Attribute("probability","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("static","sima/simo/SIMOStaticResultEntry","",True))
        self.attributes.append(BlueprintAttribute("dynamic","sima/simo/SIMODynamicResultEntry","",True))
        self.attributes.append(BlueprintAttribute("stability","sima/sima/ResultEntry","",True))
        self.attributes.append(BlueprintAttribute("preRunResults","sima/sima/ResultEntry","",True))
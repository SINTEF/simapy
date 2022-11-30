# 
# Generated with ConditionResultEntryContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.resultentrycontainer import ResultEntryContainerBlueprint
from sima.sima.blueprints.conditionresultcontainer import ConditionResultContainerBlueprint

class ConditionResultEntryContainerBlueprint(ResultEntryContainerBlueprint,ConditionResultContainerBlueprint):
    """"""

    def __init__(self, name="ConditionResultEntryContainer", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(Attribute("resource","string",""))
        self.add_attribute(Attribute("relative","boolean","",default=False))
        self.add_attribute(Attribute("changeNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("results","sima/sima/Result","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("entries","sima/sima/ResultEntry","",True,Dimension("*")))
        self.add_attribute(Attribute("modelOutputFile","string",""))
        self.add_attribute(Attribute("probability","number","",default=0.0))
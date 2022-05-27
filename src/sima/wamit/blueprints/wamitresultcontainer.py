# 
# Generated with WamitResultContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.conditionresultcontainer import ConditionResultContainerBlueprint

class WamitResultContainerBlueprint(ConditionResultContainerBlueprint):
    """"""

    def __init__(self, name="WamitResultContainer", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.attributes.append(Attribute("modelOutputFile","string","",default=""))
        self.attributes.append(Attribute("probability","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("calculationResults","sima/wamit/WamitResultEntry","",True))
        self.attributes.append(BlueprintAttribute("potenResult","sima/wamit/WamitResultEntry","",True))
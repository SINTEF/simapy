# 
# Generated with FatigueAnalysisResultContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.conditionresultcontainer import ConditionResultContainerBlueprint

class FatigueAnalysisResultContainerBlueprint(ConditionResultContainerBlueprint):
    """"""

    def __init__(self, name="FatigueAnalysisResultContainer", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("size","")))
        self.attributes.append(Attribute("modelOutputFile","string","",default=""))
        self.attributes.append(Attribute("probability","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("runResults","sima/condition/ConditionSetResultContainer","",True))
        self.attributes.append(BlueprintAttribute("fatigueResults","sima/sima/ResultEntry","",True))
# 
# Generated with MetoceanFatigueAnalysisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.condition import ConditionBlueprint

class MetoceanFatigueAnalysisBlueprint(ConditionBlueprint):
    """"""

    def __init__(self, name="MetoceanFatigueAnalysis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))
        self.attributes.append(BlueprintAttribute("metoceanCondition","sima/sima/Condition","",False))
        self.attributes.append(BlueprintAttribute("analysisCondition","sima/sima/Condition","",False))
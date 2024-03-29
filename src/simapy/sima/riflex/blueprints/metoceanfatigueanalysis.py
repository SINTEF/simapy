# 
# Generated with MetoceanFatigueAnalysisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.condition import ConditionBlueprint
from ...sima.blueprints.named import NamedBlueprint

class MetoceanFatigueAnalysisBlueprint(ConditionBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="MetoceanFatigueAnalysis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("changeNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("resultContainer","sima/sima/ResultContainer","",True))
        self.add_attribute(BlueprintAttribute("metoceanCondition","sima/sima/Condition","",False))
        self.add_attribute(BlueprintAttribute("analysisCondition","sima/sima/Condition","",False))
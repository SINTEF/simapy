# 
# Generated with ConditionSetResultContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.resultcontainer import ResultContainerBlueprint

class ConditionSetResultContainerBlueprint(ResultContainerBlueprint):
    """"""

    def __init__(self, name="ConditionSetResultContainer", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("resultContainers","sima/sima/ConditionResultContainer","",True,Dimension("*")))
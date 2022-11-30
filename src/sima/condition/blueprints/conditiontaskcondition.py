# 
# Generated with ConditionTaskConditionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.condition import ConditionBlueprint

class ConditionTaskConditionBlueprint(ConditionBlueprint):
    """"""

    def __init__(self, name="ConditionTaskCondition", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
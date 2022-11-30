# 
# Generated with ConditionRunBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class ConditionRunBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="ConditionRun", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("condition","sima/sima/Condition","",False))
        self.add_attribute(Attribute("_type","string",""))
        self.add_attribute(Attribute("addAllConditionTypes","boolean","",default=False))
        self.add_attribute(Attribute("addCustomLabel","boolean","",default=False))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("addOpenView","boolean","",default=False))
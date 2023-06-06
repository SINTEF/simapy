# 
# Generated with VariableModificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .modelvariationoperation import ModelVariationOperationBlueprint

class VariableModificationBlueprint(ModelVariationOperationBlueprint):
    """"""

    def __init__(self, name="VariableModification", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("variableItems","sima/sima/VariableItem","",True,Dimension("*")))
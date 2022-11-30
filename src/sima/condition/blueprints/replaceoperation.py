# 
# Generated with ReplaceOperationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .modelvariationoperation import ModelVariationOperationBlueprint

class ReplaceOperationBlueprint(ModelVariationOperationBlueprint):
    """"""

    def __init__(self, name="ReplaceOperation", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.add_attribute(BlueprintAttribute("replacement","sima/sima/MOAO","",True))
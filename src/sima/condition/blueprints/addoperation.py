# 
# Generated with AddOperationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .modelvariationoperation import ModelVariationOperationBlueprint

class AddOperationBlueprint(ModelVariationOperationBlueprint):
    """"""

    def __init__(self, name="AddOperation", package_path="sima/condition", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("parent","sima/sima/MOAO","",False))
        self.attributes.append(BlueprintAttribute("children","sima/sima/MOAO","",True,Dimension("*")))
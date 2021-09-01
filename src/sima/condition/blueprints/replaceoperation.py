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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.attributes.append(BlueprintAttribute("replacement","sima/sima/MOAO","",True))
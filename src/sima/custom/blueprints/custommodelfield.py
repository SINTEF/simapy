# 
# Generated with CustomModelFieldBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class CustomModelFieldBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="CustomModelField", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("tooltip","string","",default=""))
        self.attributes.append(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.attributes.append(Attribute("customTooltip","boolean","",default=False))
        self.attributes.append(Attribute("customLabel","boolean","",default=False))
        self.attributes.append(Attribute("readOnly","boolean","",default=False))
        self.attributes.append(Attribute("featureName","string","",default=""))
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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("tooltip","string",""))
        self.add_attribute(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.add_attribute(Attribute("customTooltip","boolean","",default=False))
        self.add_attribute(Attribute("customLabel","boolean","",default=False))
        self.add_attribute(Attribute("readOnly","boolean","",default=False))
        self.add_attribute(Attribute("featureName","string",""))
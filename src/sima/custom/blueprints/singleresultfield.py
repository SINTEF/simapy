# 
# Generated with SingleResultFieldBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class SingleResultFieldBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="SingleResultField", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("output","sima/post/OutputNode","",False))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("tooltip","string",""))
        self.add_attribute(Attribute("autoFormat","boolean","Format numbers automatically or choose appropriate format ",default=True))
        self.add_attribute(Attribute("format","string","Decimal numer format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description",default='0.000'))
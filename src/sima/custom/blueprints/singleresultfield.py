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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("output","sima/post/OutputNode","",False))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("tooltip","string","",default=""))
        self.attributes.append(Attribute("autoFormat","boolean","Format numbers automatically or choose appropriate format ",default=True))
        self.attributes.append(Attribute("format","string","Decimal numer format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description",default='0.000'))
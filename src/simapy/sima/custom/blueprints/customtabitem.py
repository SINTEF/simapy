# 
# Generated with CustomTabItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class CustomTabItemBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="CustomTabItem", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("children","sima/custom/CustomComponent","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string",""))
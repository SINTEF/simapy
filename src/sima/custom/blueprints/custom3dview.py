# 
# Generated with Custom3DViewBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class Custom3DViewBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="Custom3DView", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.add_attribute(Attribute("result","string",""))
        self.add_attribute(Attribute("_type","string",""))
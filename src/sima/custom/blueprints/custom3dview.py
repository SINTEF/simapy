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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.attributes.append(Attribute("result","string","",default=""))
        self.attributes.append(Attribute("_type","string","",default=""))
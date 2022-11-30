# 
# Generated with DirectInputLineTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .linetype import LineTypeBlueprint

class DirectInputLineTypeBlueprint(LineTypeBlueprint):
    """"""

    def __init__(self, name="DirectInputLineType", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("horisontalDistances","sima/simo/Distance","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("verticalDistances","sima/simo/Distance","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("items","sima/simo/TensionMap","",True,Dimension("*")))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("horisontalDistances","sima/simo/Distance","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("verticalDistances","sima/simo/Distance","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("items","sima/simo/TensionMap","",True,Dimension("size","")))
# 
# Generated with FontDescriptionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class FontDescriptionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FontDescription", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("font","string","",default=""))
        self.attributes.append(Attribute("size","integer","",default=0))
        self.attributes.append(EnumAttribute("style","sima/sima/FontStyle",""))
        self.attributes.append(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
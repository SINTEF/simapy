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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("_id","string","",default=None))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("font","string","",default=None))
        self.add_attribute(Attribute("size","integer","",default=0))
        self.add_attribute(EnumAttribute("style","sima/sima/FontStyle",""))
        self.add_attribute(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
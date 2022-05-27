# 
# Generated with HLABodyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLABodyBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLABody", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("length","number","Length",default=10.0))
        self.attributes.append(Attribute("width","number","Width",default=5.0))
        self.attributes.append(Attribute("height","number","Height",default=5.0))
        self.attributes.append(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
        self.attributes.append(BlueprintAttribute("position","sima/sima/Position","",True))
        self.attributes.append(BlueprintAttribute("viewpoints","sima/hla/HLABodyViewpoint","",True,Dimension("*")))
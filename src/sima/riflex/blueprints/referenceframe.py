# 
# Generated with ReferenceFrameBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ReferenceFrameBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ReferenceFrame", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("parent","sima/riflex/ReferenceFrame","",False))
        self.attributes.append(Attribute("xGlobal","number","Global coordinate X",default=0.0))
        self.attributes.append(Attribute("yGlobal","number","Global coordinate Y",default=0.0))
        self.attributes.append(Attribute("zGlobal","number","Global coordinate Z",default=0.0))
        self.attributes.append(Attribute("rxGlobal","number","Global  X-axis rotation",default=0.0))
        self.attributes.append(Attribute("ryGlobal","number","Global  Y-axis rotation",default=0.0))
        self.attributes.append(Attribute("rzGlobal","number","Global  Z-axis rotation",default=0.0))
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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parent","sima/riflex/ReferenceFrame","",False))
        self.add_attribute(Attribute("xGlobal","number","Global coordinate X",default=0.0))
        self.add_attribute(Attribute("yGlobal","number","Global coordinate Y",default=0.0))
        self.add_attribute(Attribute("zGlobal","number","Global coordinate Z",default=0.0))
        self.add_attribute(Attribute("rxGlobal","number","Global  X-axis rotation",default=0.0))
        self.add_attribute(Attribute("ryGlobal","number","Global  Y-axis rotation",default=0.0))
        self.add_attribute(Attribute("rzGlobal","number","Global  Z-axis rotation",default=0.0))
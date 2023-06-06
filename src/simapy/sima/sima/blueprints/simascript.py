# 
# Generated with SIMAScriptBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .namedobject import NamedObjectBlueprint

class SIMAScriptBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="SIMAScript", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("script","string",""))
        self.add_attribute(BlueprintAttribute("contextItems","sima/sima/SIMAScriptContext","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("triggers","sima/sima/SIMAScriptTrigger","",True,Dimension("*")))
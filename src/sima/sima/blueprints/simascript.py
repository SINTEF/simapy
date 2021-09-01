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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("script","string","",default=""))
        self.attributes.append(BlueprintAttribute("contextItems","sima/sima/SIMAScriptContext","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("triggers","sima/sima/SIMAScriptTrigger","",True,Dimension("size","")))
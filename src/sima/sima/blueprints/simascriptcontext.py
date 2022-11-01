# 
# Generated with SIMAScriptContextBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class SIMAScriptContextBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIMAScriptContext", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("model","sima/sima/MOAO","Model object to be directly available in script by given name",False))
        self.attributes.append(Attribute("name","string","Variable name of object that will be available in the script when evaluating",default=""))
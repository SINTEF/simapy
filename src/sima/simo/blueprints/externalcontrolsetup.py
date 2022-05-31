# 
# Generated with ExternalControlSetupBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ExternalControlSetupBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ExternalControlSetup", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("executable","string","Executable to run",default=""))
        self.attributes.append(Attribute("arguments","string","Process arguments",default=""))
        self.attributes.append(Attribute("port","integer","Port number of the central unit for the external process",default=9876))
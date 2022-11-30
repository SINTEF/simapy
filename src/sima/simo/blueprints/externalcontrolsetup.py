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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("executable","string","Executable to run"))
        self.add_attribute(Attribute("arguments","string","Process arguments"))
        self.add_attribute(Attribute("port","integer","Port number of the central unit for the external process",default=9876))
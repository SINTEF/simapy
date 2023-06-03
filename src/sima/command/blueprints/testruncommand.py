# 
# Generated with TestRunCommandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .command import CommandBlueprint

class TestRunCommandBlueprint(CommandBlueprint):
    """"""

    def __init__(self, name="TestRunCommand", package_path="sima/command", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/Property","Additional parameters",True,Dimension("*")))
        self.add_attribute(Attribute("task","string","Name of Verification task",optional=False))
        self.add_attribute(Attribute("test","string","Name of test to run",optional=False))
        self.add_attribute(Attribute("file","string","File path to export json status report"))
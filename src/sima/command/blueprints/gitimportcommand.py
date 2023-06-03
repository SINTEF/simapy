# 
# Generated with GitImportCommandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .command import CommandBlueprint

class GitImportCommandBlueprint(CommandBlueprint):
    """"""

    def __init__(self, name="GitImportCommand", package_path="sima/command", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/Property","Additional parameters",True,Dimension("*")))
        self.add_attribute(Attribute("uri","string","URI of the git repository"))
        self.add_attribute(Attribute("branch","string","Branch name",default='master'))
        self.add_attribute(Attribute("location","string","location of repository on disk (default is within workspace)"))
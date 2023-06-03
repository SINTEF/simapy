# 
# Generated with ExportCommandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .command import CommandBlueprint

class ExportCommandBlueprint(CommandBlueprint):
    """"""

    def __init__(self, name="ExportCommand", package_path="sima/command", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/Property","Additional parameters",True,Dimension("*")))
        self.add_attribute(Attribute("file","string","Path to file, e.g stask",optional=False))
        self.add_attribute(Attribute("delete","boolean","Delete the file if it already exist",default=False))
        self.add_attribute(Attribute("dependencies","boolean","Include task dependencies automatically",default=True))
        self.add_attribute(Attribute("tasks","string","Optional list of task names to export (if not given all tasks will be exported)",Dimension("*")))
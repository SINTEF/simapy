# 
# Generated with ConditionRunCommandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .command import CommandBlueprint

class ConditionRunCommandBlueprint(CommandBlueprint):
    """"""

    def __init__(self, name="ConditionRunCommand", package_path="sima/command", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/Property","Additional parameters",True,Dimension("*")))
        self.add_attribute(Attribute("task","string","Name of task containing condition",optional=False))
        self.add_attribute(Attribute("condition","string","Name of condition to run",optional=False))
        self.add_attribute(Attribute("runType","string","Condition run type",optional=False))
        self.add_attribute(Attribute("dir","string","Optional working directory ( may be specified with sima resource urls: sima:// which are relative to the workspace).\nIf the working directory is given outside the workspace SIMA will not delete any of the files before running."))
        self.add_attribute(Attribute("output","string","If set will export all the condition results to the given file"))
        self.add_attribute(BlueprintAttribute("input","sima/sima/Property","Enables override of condition variables. Specify variable name and wanted value",True,Dimension("*")))
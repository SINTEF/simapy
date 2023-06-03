# 
# Generated with WorkflowInputCommandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .command import CommandBlueprint

class WorkflowInputCommandBlueprint(CommandBlueprint):
    """"""

    def __init__(self, name="WorkflowInputCommand", package_path="sima/command", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/Property","Additional parameters",True,Dimension("*")))
        self.add_attribute(Attribute("task","string","Name of task containing workflow",optional=False))
        self.add_attribute(Attribute("workflow","string","Workflow name",optional=False))
        self.add_attribute(BlueprintAttribute("input","sima/sima/Property","Enables override of task variables or workflow input values.\nSpecified on the form Hs=2.0;Tp=12.0 where Hs and Tp are names of variables or workflow inputs.\nVariables will take precendence if duplicate names exist.\nIt is also possible to specify more complex input by using the json string representation of SIMA signals.",True,Dimension("*")))
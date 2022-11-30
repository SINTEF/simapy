# 
# Generated with CustomWorkflowSetInputBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class CustomWorkflowSetInputBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="CustomWorkflowSetInput", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("workflowSet","sima/workflow/WorkflowSetNode","",False))
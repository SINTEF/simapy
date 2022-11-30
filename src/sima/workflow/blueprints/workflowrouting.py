# 
# Generated with WorkflowRoutingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WorkflowRoutingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WorkflowRouting", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("workflowSetInputs","sima/workflow/WorkflowSetItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("workflowInputVariations","sima/workflow/WorkflowInputVariationItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("inputs","sima/workflow/WorkflowLinkItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("outputs","sima/workflow/WorkflowLinkItem","",True,Dimension("*")))
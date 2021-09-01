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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("workflowSetInputs","sima/workflow/WorkflowSetItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("workflowInputVariations","sima/workflow/WorkflowInputVariationItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("inputs","sima/workflow/WorkflowLinkItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("outputs","sima/workflow/WorkflowLinkItem","",True,Dimension("size","")))
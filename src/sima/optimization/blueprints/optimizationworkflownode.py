# 
# Generated with OptimizationWorkflowNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.workflow.blueprints.workflowreferencenode import WorkflowReferenceNodeBlueprint

class OptimizationWorkflowNodeBlueprint(WorkflowReferenceNodeBlueprint):
    """"""

    def __init__(self, name="OptimizationWorkflowNode", package_path="sima/optimization", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("variableInputSlots","sima/workflow/VariableInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("modelReferenceInputSlot","sima/workflow/ModelReferenceInputSlot","",True))
        self.add_attribute(BlueprintAttribute("workflow","sima/workflow/Workflow","",False))
        self.add_attribute(BlueprintAttribute("workflowOutputSlots","sima/workflow/WorkflowOutputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("workflowInputSlots","sima/workflow/WorkflowInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("inputWorkflow","boolean","Set the workflow input from the outside. Use a model reference as source.",default=False))
        self.add_attribute(Attribute("setFolderName","boolean","Override the default folder name created. This folder will be relative to the running workflow. If left empty it will create the results directly in the workflow folder.",default=False))
        self.add_attribute(Attribute("folderName","string",""))
        self.add_attribute(BlueprintAttribute("optimizationCalculationParameters","sima/optimization/OptimizationCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("costFunction","sima/workflow/WorkflowOutput","",False))
        self.add_attribute(BlueprintAttribute("constraints","sima/workflow/WorkflowOutput","",False))
        self.add_attribute(BlueprintAttribute("variableItems","sima/optimization/OptimizationVariableItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("result","sima/workflow/WorkflowOutputSlot","",True))
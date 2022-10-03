# 
# Generated with DoWhileNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .workflowreferencenode import WorkflowReferenceNodeBlueprint

class DoWhileNodeBlueprint(WorkflowReferenceNodeBlueprint):
    """"""

    def __init__(self, name="DoWhileNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("variableInputSlots","sima/workflow/VariableInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("modelReferenceInputSlot","sima/workflow/ModelReferenceInputSlot","",True))
        self.attributes.append(BlueprintAttribute("workflow","sima/workflow/Workflow","",False))
        self.attributes.append(BlueprintAttribute("workflowOutputSlots","sima/workflow/WorkflowOutputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("workflowInputSlots","sima/workflow/WorkflowInputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("inputWorkflow","boolean","Set the workflow input from the outside. Use a model reference as source.",default=False))
        self.attributes.append(Attribute("setFolderName","boolean","Override the default folder name created. This folder will be relative to the running workflow. If left empty it will create the results directly in the workflow folder.",default=False))
        self.attributes.append(Attribute("folderName","string","",default=""))
        self.attributes.append(BlueprintAttribute("loopWhile","sima/workflow/WorkflowOutput","Loop while given condition/constraint is true. All constraints must be true to finish (and operation)",False))
        self.attributes.append(Attribute("maxIterations","integer","If set, the iteration will stop when maximum number of iterations is reached",default=0))
        self.attributes.append(BlueprintAttribute("plot","sima/workflow/WorkflowOutput","Can be used to show live plot if needed as a debug step",False))
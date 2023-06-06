# 
# Generated with WorkflowSetNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .workflowreferencenode import WorkflowReferenceNodeBlueprint

class WorkflowSetNodeBlueprint(WorkflowReferenceNodeBlueprint):
    """"""

    def __init__(self, name="WorkflowSetNode", package_path="sima/workflow", description=""):
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
        self.add_attribute(BlueprintAttribute("variableInputSets","sima/workflow/VariableInputSet","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("variableInputSetSlots","sima/workflow/VariableInputSetSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("writeRunStatus","boolean","Write a text file with the run status after running all the cases",default=False))
        self.add_attribute(Attribute("runStatusFolder","string","If provided the status file(s) will  to exported to this location"))
        self.add_attribute(EnumAttribute("input","sima/workflow/WorkflowSetInput","Specify variable values from file."))
        self.add_attribute(Attribute("filename","string","Import variable values from file. Expected file format:\n' any comment specified with '\n'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  \n1.0      2.0    3\n4.0      5.0    4\n'any comment\n           "))
        self.add_attribute(EnumAttribute("iteration","sima/workflow/Iteration","Switch to change type of iteration"))
        self.add_attribute(Attribute("distribute","boolean","Distribute workflow using SIMACompute",default=False))
        self.add_attribute(Attribute("grouping","integer","Group given amount of runs together in the same process. Should be used if workflow within takes a relative short amount of time compared to forking off a new process",default=1))
        self.add_attribute(Attribute("iterateOverInput","boolean","Enable iteration over workflow inputs. The iteration will loop over all input folders with type=workflow",default=False))
        self.add_attribute(BlueprintAttribute("workflowInputVariationSlots","sima/workflow/WorkflowInputSlot","",True,Dimension("*")))
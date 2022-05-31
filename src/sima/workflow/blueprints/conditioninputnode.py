# 
# Generated with ConditionInputNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class ConditionInputNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="ConditionInputNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("variableInputSlots","sima/workflow/VariableInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("modelReferenceInputSlot","sima/workflow/ModelReferenceInputSlot","",True))
        self.attributes.append(BlueprintAttribute("condition","sima/sima/Condition","",False))
        self.attributes.append(Attribute("analysis","string","",default=""))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(BlueprintAttribute("additionalFiles","sima/workflow/FileSpecification","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("modelOutput","sima/workflow/ModelOutputSpecification","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("modelInputSlots","sima/workflow/ModelInputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("inputCondition","boolean","Set the condition input from the outside. Use a model reference as source.",default=False))
        self.attributes.append(Attribute("setFolderName","boolean","Override the default folder name created. This folder will be relative to the running workflow. If left empty it will create the results directly in the workflow folder.",default=False))
        self.attributes.append(Attribute("folderName","string","",default=""))
        self.attributes.append(Attribute("addInputFiles","boolean","Add additional input files before running",default=False))
        self.attributes.append(BlueprintAttribute("fileInputSlot","sima/post/InputSlot","",True))
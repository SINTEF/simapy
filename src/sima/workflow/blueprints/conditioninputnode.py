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
        self.add_attribute(BlueprintAttribute("condition","sima/sima/Condition","",False))
        self.add_attribute(Attribute("analysis","string",""))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(BlueprintAttribute("additionalFiles","sima/workflow/FileSpecification","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("modelOutput","sima/workflow/ModelOutputSpecification","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("modelInputSlots","sima/workflow/ModelInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("inputCondition","boolean","Set the condition input from the outside. Use a model reference as source.",default=False))
        self.add_attribute(Attribute("setFolderName","boolean","Override the default folder name created. This folder will be relative to the running workflow. If left empty it will create the results directly in the workflow folder.",default=False))
        self.add_attribute(Attribute("folderName","string",""))
        self.add_attribute(Attribute("addInputFiles","boolean","Add additional input files before running",default=False))
        self.add_attribute(BlueprintAttribute("fileInputSlot","sima/post/InputSlot","",True))
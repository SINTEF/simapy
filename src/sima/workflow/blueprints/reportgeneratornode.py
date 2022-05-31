# 
# Generated with ReportGeneratorNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class ReportGeneratorNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="ReportGeneratorNode", package_path="sima/workflow", description=""):
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
        self.attributes.append(BlueprintAttribute("report","sima/report/Report","",False))
        self.attributes.append(BlueprintAttribute("fragmentInputSlots","sima/workflow/ReportFragmentReferenceInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(Attribute("inputReport","boolean","Set the report input from the outside. Use a model reference as source.",default=False))
        self.attributes.append(EnumAttribute("format","sima/workflow/ReportFormat",""))
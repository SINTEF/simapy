# 
# Generated with ModelReferenceInputBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .valueinputnode import ValueInputNodeBlueprint
from .modelreference import ModelReferenceBlueprint

class ModelReferenceInputBlueprint(ValueInputNodeBlueprint,ModelReferenceBlueprint):
    """"""

    def __init__(self, name="ModelReferenceInput", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("root","string",""))
        self.add_attribute(Attribute("resultId","string",""))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.add_attribute(Attribute("reference","string","",default='workflow'))
        self.add_attribute(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the signal",default=False))
        self.add_attribute(Attribute("_type","string","",default='workflow'))
        self.add_attribute(Attribute("useReference","boolean","Uses a soft link to the referenced model, meaning the relation is not cleared if the references object is deleted or does not exist",default=False))
        self.add_attribute(Attribute("array","boolean","Create an array output",default=False))
        self.add_attribute(BlueprintAttribute("modelReferences","sima/workflow/ModelReference","",True,Dimension("*")))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("size","")))
        self.attributes.append(Attribute("root","string","",default=""))
        self.attributes.append(Attribute("resultId","string","",default=""))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("model","sima/sima/MOAO","",False))
        self.attributes.append(Attribute("reference","string","",default='workflow'))
        self.attributes.append(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the signal",default=False))
        self.attributes.append(Attribute("_type","string","",default='workflow'))
        self.attributes.append(Attribute("useReference","boolean","Uses a soft link to the referenced model, meaning the relation is not cleared if the references object is deleted or does not exist",default=False))
        self.attributes.append(Attribute("array","boolean","Create an array output",default=False))
        self.attributes.append(BlueprintAttribute("modelReferences","sima/workflow/ModelReference","",True,Dimension("size","")))
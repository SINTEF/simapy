# 
# Generated with TextInputBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .valueinputnode import ValueInputNodeBlueprint

class TextInputBlueprint(ValueInputNodeBlueprint):
    """"""

    def __init__(self, name="TextInput", package_path="sima/workflow", description=""):
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
        self.attributes.append(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the signal",default=False))
        self.attributes.append(Attribute("value","string","",default=""))
        self.attributes.append(Attribute("array","boolean","Create a text array output",default=False))
        self.attributes.append(Attribute("values","string","",Dimension("size",""),default=""))
# 
# Generated with IntegerInputBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .valueinputnode import ValueInputNodeBlueprint

class IntegerInputBlueprint(ValueInputNodeBlueprint):
    """"""

    def __init__(self, name="IntegerInput", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("_id","string","",default=None))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string","",default=None))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("root","string","",default=None))
        self.add_attribute(Attribute("resultId","string","",default=None))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the signal",default=False))
        self.add_attribute(Attribute("value","integer","",default=0))
# 
# Generated with NumberSignalInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .controlsignalinputslot import ControlSignalInputSlotBlueprint

class NumberSignalInputSlotBlueprint(ControlSignalInputSlotBlueprint):
    """"""

    def __init__(self, name="NumberSignalInputSlot", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the signal",default=False))
        self.add_attribute(Attribute("array","boolean","",default=False))
        self.add_attribute(Attribute("value","number","",default=0.0))
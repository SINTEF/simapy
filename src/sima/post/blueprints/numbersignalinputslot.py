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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("size","")))
        self.attributes.append(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the signal",default=False))
        self.attributes.append(Attribute("array","boolean","",default=False))
        self.attributes.append(Attribute("value","number","",default=0.0))
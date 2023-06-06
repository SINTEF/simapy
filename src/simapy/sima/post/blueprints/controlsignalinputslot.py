# 
# Generated with ControlSignalInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .inputslot import InputSlotBlueprint
from .signalpropertiescontainer import SignalPropertiesContainerBlueprint

class ControlSignalInputSlotBlueprint(InputSlotBlueprint,SignalPropertiesContainerBlueprint):
    """"""

    def __init__(self, name="ControlSignalInputSlot", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
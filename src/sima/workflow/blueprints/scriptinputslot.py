# 
# Generated with ScriptInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.inputslot import InputSlotBlueprint
from sima.post.blueprints.signalpropertiescontainer import SignalPropertiesContainerBlueprint

class ScriptInputSlotBlueprint(InputSlotBlueprint,SignalPropertiesContainerBlueprint):
    """"""

    def __init__(self, name="ScriptInputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("inputSignals","boolean","If checked the input will be imported directly as signals in an array with name as specified.",default=False))
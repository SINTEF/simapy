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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.attributes.append(Attribute("inputSignals","boolean","If checked the input will be imported directly as signals in an array with name as specified.",default=False))
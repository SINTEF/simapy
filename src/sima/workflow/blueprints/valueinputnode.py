# 
# Generated with ValueInputNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .workflowinput import WorkflowInputBlueprint
from sima.post.blueprints.signalpropertiescontainer import SignalPropertiesContainerBlueprint
from sima.sima.blueprints.singleparameter import SingleParameterBlueprint

class ValueInputNodeBlueprint(WorkflowInputBlueprint,SignalPropertiesContainerBlueprint,SingleParameterBlueprint):
    """"""

    def __init__(self, name="ValueInputNode", package_path="sima/workflow", description=""):
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
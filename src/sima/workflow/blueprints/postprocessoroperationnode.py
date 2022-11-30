# 
# Generated with PostProcessorOperationNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class PostProcessorOperationNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="PostProcessorOperationNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("nodes","sima/post/OperationNode","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("connections","sima/post/SlotConnection","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("operation","sima/post/OperationNode","",False))
        self.add_attribute(BlueprintAttribute("operationOutputSlots","sima/workflow/OperationOutputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("operationInputSlots","sima/workflow/OperationInputSlot","",True,Dimension("*")))
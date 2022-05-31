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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("nodes","sima/post/OperationNode","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("connections","sima/post/SlotConnection","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("operation","sima/post/OperationNode","",False))
        self.attributes.append(BlueprintAttribute("operationOutputSlots","sima/workflow/OperationOutputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("operationInputSlots","sima/workflow/OperationInputSlot","",True,Dimension("*")))
# 
# Generated with PostProcessorNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class PostProcessorNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="PostProcessorNode", package_path="sima/workflow", description=""):
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
        self.attributes.append(BlueprintAttribute("variableInputSlots","sima/workflow/VariableInputSlot","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("postprocessor","sima/post/PostProcessorSpecification","",False))
        self.attributes.append(BlueprintAttribute("postOutputSlots","sima/workflow/PostprocessorOutputSlot","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("postInputSlots","sima/workflow/PostprocessorInputSlot","",True,Dimension("size","")))
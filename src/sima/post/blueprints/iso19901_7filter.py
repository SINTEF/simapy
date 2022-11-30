# 
# Generated with ISO19901_7FilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class ISO19901_7FilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="ISO19901_7Filter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.add_attribute(Attribute("customSafetyFactor","number","Safety factor",default=0.0))
        self.add_attribute(EnumAttribute("analysis","sima/post/ISO19901_7_analysis",""))
        self.add_attribute(EnumAttribute("mooringType","sima/post/MooringType",""))
        self.add_attribute(EnumAttribute("consequenceClass","sima/post/ConsequenceClass",""))
        self.add_attribute(Attribute("useCustomSafetyFactor","boolean","",default=False))
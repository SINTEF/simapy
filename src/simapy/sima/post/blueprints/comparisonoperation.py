# 
# Generated with ComparisonOperationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class ComparisonOperationBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="ComparisonOperation", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("first","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("second","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(Attribute("factor","number","Compares two values by using a factor times the smallest of the two numbers",default=1e-05))
        self.add_attribute(Attribute("threshold","number","Values less than this number is considered zero",default=1e-15))
        self.add_attribute(Attribute("fail","boolean","If checked the operation will fail the current run when the inputs are different",default=True))
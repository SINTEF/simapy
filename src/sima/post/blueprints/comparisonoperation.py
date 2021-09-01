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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("first","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("second","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(Attribute("factor","number","Compares two values by using a factor times the smallest of the two numbers",default=1e-05))
        self.attributes.append(Attribute("threshold","number","Values less than this number is considered zero",default=1e-15))
        self.attributes.append(Attribute("fail","boolean","If checked the operation will fail the current run when the inputs are different",default=True))
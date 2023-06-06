# 
# Generated with ISO13628_7FilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class ISO13628_7FilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="ISO13628_7Filter", package_path="sima/post", description=""):
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
        self.add_attribute(Attribute("ultimateTensionCapacity","number","Single load ultimate tension capacity",default=0.0))
        self.add_attribute(Attribute("ultimateBendingCapacity","number","Single load ultimate bending capacity",default=0.0))
        self.add_attribute(Attribute("ultimatePressureCapacity","number","Single load ultimate pressure capacity due to end cap effect",default=0.0))
        self.add_attribute(Attribute("internalPressure","number","Internal pressure",default=0.0))
        self.add_attribute(Attribute("externalPressure","number","External pressure",default=0.0))
        self.add_attribute(Attribute("designFactor","number","Design factor",default=0.8))
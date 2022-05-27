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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("ultimateTensionCapacity","number","Single load ultimate tension capacity",default=0.0))
        self.attributes.append(Attribute("ultimateBendingCapacity","number","Single load ultimate bending capacity",default=0.0))
        self.attributes.append(Attribute("ultimatePressureCapacity","number","Single load ultimate pressure capacity due to end cap effect",default=0.0))
        self.attributes.append(Attribute("internalPressure","number","Internal pressure",default=0.0))
        self.attributes.append(Attribute("externalPressure","number","External pressure",default=0.0))
        self.attributes.append(Attribute("designFactor","number","Design factor",default=0.8))
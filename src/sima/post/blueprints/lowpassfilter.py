# 
# Generated with LowPassFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class LowPassFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="LowPassFilter", package_path="sima/post", description=""):
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
        self.attributes.append(Attribute("renameOutput","boolean","",default=True))
        self.attributes.append(Attribute("taperingFactor","number","Exponent in tapering of coefficient",default=0.5))
        self.attributes.append(Attribute("coefficientCount","integer","Number of coefficients. If not set it will be set to round(k/(2*dt*fCut))",default=0))
        self.attributes.append(Attribute("normalizedWindowDuration","integer","normalized window duration: k. Used to calculate default coefficientCount",default=4))
        self.attributes.append(Attribute("cutoffFrequency","number","Cut off frequency",default=0.0))
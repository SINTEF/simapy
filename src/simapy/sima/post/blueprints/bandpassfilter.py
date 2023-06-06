# 
# Generated with BandPassFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class BandPassFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="BandPassFilter", package_path="sima/post", description=""):
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
        self.add_attribute(Attribute("renameOutput","boolean","",default=True))
        self.add_attribute(Attribute("taperingFactor","number","Exponent in tapering of coefficient",default=0.5))
        self.add_attribute(Attribute("coefficientCount","integer","Number of coefficients. If not set it will be set to round(k/(2*dt*fCut))",default=0))
        self.add_attribute(Attribute("normalizedWindowDuration","integer","normalized window duration: k. Used to calculate default coefficientCount",default=4))
        self.add_attribute(Attribute("lowerCutoffFrequency","number","Lower cut off frequency",default=0.0))
        self.add_attribute(Attribute("upperCutoffFrequency","number","Upper cut off frequency",default=0.0))
# 
# Generated with AutoSpectrumFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class AutoSpectrumFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="AutoSpectrumFilter", package_path="sima/post", description=""):
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
        self.attributes.append(Attribute("subtractMean","boolean","Subtract mean value from input",default=False))
        self.attributes.append(Attribute("smoothingParameter","integer","Smoothing parameter",default=3))
        self.attributes.append(Attribute("fadedOverlap","boolean","Faded overlap coefficient",default=False))
        self.attributes.append(Attribute("numPointsFFT","integer","Number of points to be used in fft (default is all input points)",default=0))
        self.attributes.append(Attribute("taperWindowLength","number","Relative length of cosine taper window",default=0.1))
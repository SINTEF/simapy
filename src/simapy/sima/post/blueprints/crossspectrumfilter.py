# 
# Generated with CrossSpectrumFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class CrossSpectrumFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="CrossSpectrumFilter", package_path="sima/post", description=""):
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
        self.add_attribute(Attribute("subtractMean","boolean","Subtract mean value from input",default=False))
        self.add_attribute(Attribute("smoothingParameter","integer","Smoothing parameter",default=3))
        self.add_attribute(Attribute("fadedOverlap","boolean","Faded overlap coefficient",default=False))
        self.add_attribute(Attribute("numPointsFFT","integer","Number of points to be used in fft (default is all input points)",default=0))
        self.add_attribute(Attribute("taperWindowLength","number","Relative length of cosine taper window",default=0.1))
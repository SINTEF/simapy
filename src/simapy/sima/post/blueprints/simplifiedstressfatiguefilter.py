# 
# Generated with SimplifiedStressFatigueFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class SimplifiedStressFatigueFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="SimplifiedStressFatigueFilter", package_path="sima/post", description=""):
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
        self.add_attribute(Attribute("numberOfPoints","integer","Number of points in the calculation",default=8))
        self.add_attribute(Attribute("radius","number","Distance from pipe center to a point in the pipe wall",default=0.0))
        self.add_attribute(Attribute("innerRadius","number","Inner radius of the pipe",default=0.0))
        self.add_attribute(Attribute("outerRadius","number","Outer radius of the pipe",default=0.0))
        self.add_attribute(Attribute("numberOfCycles","integer","Number of cycles",default=0))
        self.add_attribute(Attribute("shape","number","Shape parameter of stress distribution",default=0.0))
        self.add_attribute(Attribute("intercept","number","Intercept parameter of the SN curve",default=0.0))
        self.add_attribute(Attribute("slope","number","Slope parameter of the SN curve",default=0.0))
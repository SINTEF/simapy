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
        self.attributes.append(Attribute("numberOfPoints","integer","Number of points in the calculation",default=8))
        self.attributes.append(Attribute("radius","number","Distance from pipe center to a point in the pipe wall",default=0.0))
        self.attributes.append(Attribute("innerRadius","number","Inner radius of the pipe",default=0.0))
        self.attributes.append(Attribute("outerRadius","number","Outer radius of the pipe",default=0.0))
        self.attributes.append(Attribute("numberOfCycles","integer","Number of cycles",default=0))
        self.attributes.append(Attribute("shape","number","Shape parameter of stress distribution",default=0.0))
        self.attributes.append(Attribute("intercept","number","Intercept parameter of the SN curve",default=0.0))
        self.attributes.append(Attribute("slope","number","Slope parameter of the SN curve",default=0.0))
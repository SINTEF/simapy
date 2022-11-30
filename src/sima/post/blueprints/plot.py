# 
# Generated with PlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint
from .outputnode import OutputNodeBlueprint

class PlotBlueprint(OperationNodeBlueprint,OutputNodeBlueprint):
    """"""

    def __init__(self, name="Plot", package_path="sima/post", description=""):
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
        self.add_attribute(BlueprintAttribute("figureTemplate","sima/post/FigureTemplate","",True))
        self.add_attribute(BlueprintAttribute("traces","sima/post/TraceConfiguration","",True,Dimension("*")))
        self.add_attribute(Attribute("fixed","boolean","",default=False))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("xLabel","string",""))
        self.add_attribute(Attribute("yLabel","string",""))
        self.add_attribute(Attribute("selectAll","boolean","Will export all signals as plot",default=False))
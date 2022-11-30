# 
# Generated with PlotNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.outputnode import OutputNodeBlueprint

class PlotNodeBlueprint(OutputNodeBlueprint):
    """"""

    def __init__(self, name="PlotNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("figureTemplate","sima/post/FigureTemplate","",True))
        self.add_attribute(BlueprintAttribute("traces","sima/post/TraceConfiguration","",True,Dimension("*")))
        self.add_attribute(Attribute("fixed","boolean","",default=False))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("xLabel","string",""))
        self.add_attribute(Attribute("yLabel","string",""))
        self.add_attribute(Attribute("selectAll","boolean","Will export all signals as plot",default=False))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(Attribute("createImages","boolean","Create images and store these to disk. The output will then be the paths to the images",default=True))
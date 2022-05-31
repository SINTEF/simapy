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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("figureTemplate","sima/post/FigureTemplate","",True))
        self.attributes.append(BlueprintAttribute("traces","sima/post/TraceConfiguration","",True,Dimension("*")))
        self.attributes.append(Attribute("fixed","boolean","",default=False))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("xLabel","string","",default=""))
        self.attributes.append(Attribute("yLabel","string","",default=""))
        self.attributes.append(Attribute("selectAll","boolean","Will export all signals as plot",default=False))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(Attribute("createImages","boolean","Create images and store these to disk. The output will then be the paths to the images",default=True))
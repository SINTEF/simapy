# 
# Generated with FigureTemplateBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FigureTemplateBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FigureTemplate", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("titleFont","sima/sima/FontDescription","",True))
        self.add_attribute(BlueprintAttribute("legendFont","sima/sima/FontDescription","",True))
        self.add_attribute(BlueprintAttribute("xAxis","sima/post/AxisConfiguration","",True))
        self.add_attribute(BlueprintAttribute("yAxis","sima/post/AxisConfiguration","",True))
        self.add_attribute(Attribute("showTitle","boolean","",default=True))
        self.add_attribute(Attribute("showLegend","boolean","",default=True))
        self.add_attribute(EnumAttribute("size","sima/post/PlotSize",""))
        self.add_attribute(Attribute("width","integer","",default=0))
        self.add_attribute(Attribute("height","integer","",default=0))
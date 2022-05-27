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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("titleFont","sima/sima/FontDescription","",True))
        self.attributes.append(BlueprintAttribute("legendFont","sima/sima/FontDescription","",True))
        self.attributes.append(BlueprintAttribute("xAxis","sima/post/AxisConfiguration","",True))
        self.attributes.append(BlueprintAttribute("yAxis","sima/post/AxisConfiguration","",True))
        self.attributes.append(Attribute("showTitle","boolean","",default=True))
        self.attributes.append(Attribute("showLegend","boolean","",default=True))
        self.attributes.append(EnumAttribute("size","sima/post/PlotSize",""))
        self.attributes.append(Attribute("width","integer","",default=0))
        self.attributes.append(Attribute("height","integer","",default=0))
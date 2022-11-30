# 
# Generated with LinePlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class LinePlotBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="LinePlot", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("xlabel","string",""))
        self.add_attribute(Attribute("ylabel","string",""))
        self.add_attribute(Attribute("showlegend","boolean","",default=True))
        self.add_attribute(Attribute("showtitle","boolean","",default=True))
        self.add_attribute(Attribute("caption","string",""))
        self.add_attribute(Attribute("width","integer","",default=0))
        self.add_attribute(Attribute("height","integer","",default=0))
        self.add_attribute(EnumAttribute("size","marmo/report/PlotSize",""))
        self.add_attribute(BlueprintAttribute("titlefont","marmo/report/Font","",True))
        self.add_attribute(BlueprintAttribute("legendfont","marmo/report/Font","",True))
        self.add_attribute(BlueprintAttribute("xaxis","marmo/report/Axis","",True))
        self.add_attribute(BlueprintAttribute("yaxis","marmo/report/Axis","",True))
        self.add_attribute(BlueprintAttribute("lines","marmo/report/PlotLine","",True,Dimension("*")))
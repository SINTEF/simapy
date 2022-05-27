# 
# Generated with LinePlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class LinePlotBlueprint(Blueprint):
    """"""

    def __init__(self, name="LinePlot", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("xlabel","string","",default=""))
        self.attributes.append(Attribute("ylabel","string","",default=""))
        self.attributes.append(Attribute("showlegend","boolean","",default=True))
        self.attributes.append(Attribute("showtitle","boolean","",default=True))
        self.attributes.append(Attribute("caption","string","",default=""))
        self.attributes.append(Attribute("width","integer","",default=0))
        self.attributes.append(Attribute("height","integer","",default=0))
        self.attributes.append(EnumAttribute("size","marmo/report/PlotSize",""))
        self.attributes.append(BlueprintAttribute("titlefont","marmo/report/Font","",True))
        self.attributes.append(BlueprintAttribute("legendfont","marmo/report/Font","",True))
        self.attributes.append(BlueprintAttribute("xaxis","marmo/report/Axis","",True))
        self.attributes.append(BlueprintAttribute("yaxis","marmo/report/Axis","",True))
        self.attributes.append(BlueprintAttribute("lines","marmo/report/PlotLine","",True,Dimension("*")))
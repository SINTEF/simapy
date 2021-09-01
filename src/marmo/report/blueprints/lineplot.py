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
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("title","string",""))
        self.attributes.append(Attribute("xlabel","string",""))
        self.attributes.append(Attribute("ylabel","string",""))
        self.attributes.append(Attribute("showlegend","boolean",""))
        self.attributes.append(Attribute("showtitle","boolean",""))
        self.attributes.append(Attribute("caption","string",""))
        self.attributes.append(Attribute("width","integer",""))
        self.attributes.append(Attribute("height","integer",""))
        self.attributes.append(EnumAttribute("size","string",""))
        self.attributes.append(BlueprintAttribute("titlefont","/report/Font","",True))
        self.attributes.append(BlueprintAttribute("legendfont","/report/Font","",True))
        self.attributes.append(BlueprintAttribute("xaxis","/report/Axis","",True))
        self.attributes.append(BlueprintAttribute("yaxis","/report/Axis","",True))
        self.attributes.append(BlueprintAttribute("lines","/report/PlotLine","",True,Dimension("size","")))
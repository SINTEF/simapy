# 
# Generated with PlotLineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class PlotLineBlueprint(Blueprint):
    """"""

    def __init__(self, name="PlotLine", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("xlabel","string","",default=""))
        self.attributes.append(Attribute("ylabel","string","",default=""))
        self.attributes.append(Attribute("showlegend","boolean","",default=True))
        self.attributes.append(Attribute("x","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("y","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("linewidth","integer","",default=1))
        self.attributes.append(Attribute("pointsize","integer","",default=1))
        self.attributes.append(EnumAttribute("linestyle","marmo/report/LineStyle",""))
        self.attributes.append(EnumAttribute("pointstyle","marmo/report/PointStyle",""))
        self.attributes.append(Attribute("color","string","",default=""))
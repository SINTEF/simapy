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
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("xlabel","string",""))
        self.attributes.append(Attribute("ylabel","string",""))
        self.attributes.append(Attribute("showlegend","boolean",""))
        self.attributes.append(Attribute("x","number","",Dimension("size","")))
        self.attributes.append(Attribute("y","number","",Dimension("size","")))
        self.attributes.append(Attribute("linewidth","integer",""))
        self.attributes.append(Attribute("pointsize","integer",""))
        self.attributes.append(EnumAttribute("linestyle","string",""))
        self.attributes.append(EnumAttribute("pointstyle","string",""))
        self.attributes.append(Attribute("color","string",""))
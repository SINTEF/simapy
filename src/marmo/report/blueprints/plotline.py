# 
# Generated with PlotLineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class PlotLineBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="PlotLine", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("xlabel","string",""))
        self.add_attribute(Attribute("ylabel","string",""))
        self.add_attribute(Attribute("showlegend","boolean","",default=True))
        self.add_attribute(Attribute("x","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("y","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("linewidth","integer","",default=1))
        self.add_attribute(Attribute("pointsize","integer","",default=1))
        self.add_attribute(EnumAttribute("linestyle","marmo/report/LineStyle",""))
        self.add_attribute(EnumAttribute("pointstyle","marmo/report/PointStyle",""))
        self.add_attribute(Attribute("color","string",""))
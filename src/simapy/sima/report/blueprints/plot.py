# 
# Generated with PlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class PlotBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="Plot", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("object","sima/sima/MOAO","",False))
        self.add_attribute(Attribute("caption","string","Caption"))
        self.add_attribute(Attribute("mergeSeries","boolean","Merge all series in one plot",default=False))
        self.add_attribute(Attribute("xLabel","string",""))
        self.add_attribute(Attribute("yLabel","string",""))
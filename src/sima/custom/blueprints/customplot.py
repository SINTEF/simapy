# 
# Generated with CustomPlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class CustomPlotBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="CustomPlot", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("output","sima/post/OutputNode","",False))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("showTree","boolean","",default=False))
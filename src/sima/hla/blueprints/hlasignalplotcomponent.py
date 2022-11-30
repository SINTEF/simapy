# 
# Generated with HLASignalPlotComponentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.custom.blueprints.customcomponent import CustomComponentBlueprint

class HLASignalPlotComponentBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="HLASignalPlotComponent", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("plot","sima/hla/HLASignalPlot","",False))
# 
# Generated with HLASignalPlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class HLASignalPlotBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="HLASignalPlot", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("figureTemplate","sima/post/FigureTemplate","",True))
        self.add_attribute(BlueprintAttribute("traces","sima/post/TraceConfiguration","",True,Dimension("*")))
        self.add_attribute(Attribute("fixed","boolean","",default=False))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("xLabel","string",""))
        self.add_attribute(Attribute("yLabel","string",""))
        self.add_attribute(Attribute("selectAll","boolean","Will export all signals as plot",default=False))
        self.add_attribute(BlueprintAttribute("signals","sima/hla/HLASignal","",True,Dimension("*")))
        self.add_attribute(Attribute("timeWindow","number","Maximum size of time window when displaying plot.",default=60.0))
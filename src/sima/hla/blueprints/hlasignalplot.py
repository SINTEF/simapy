# 
# Generated with HLASignalPlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class HLASignalPlotBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="HLASignalPlot", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("figureTemplate","sima/post/FigureTemplate","",True))
        self.attributes.append(BlueprintAttribute("traces","sima/post/TraceConfiguration","",True,Dimension("size","")))
        self.attributes.append(Attribute("fixed","boolean","",default=False))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("xLabel","string","",default=""))
        self.attributes.append(Attribute("yLabel","string","",default=""))
        self.attributes.append(Attribute("selectAll","boolean","Will export all signals as plot",default=False))
        self.attributes.append(BlueprintAttribute("signals","sima/hla/HLASignal","",True,Dimension("size","")))
        self.attributes.append(Attribute("timeWindow","number","Maximum size of time window when displaying plot.",default=60.0))
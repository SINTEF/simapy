# 
# Generated with HLAPlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLAPlotBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLAPlot", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("_id","string","",default=None))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string","",default=None))
        self.add_attribute(Attribute("curves","string","",Dimension("*"),default=None))
        self.add_attribute(Attribute("crossPlotXAxisValues","string","",default=None))
        self.add_attribute(BlueprintAttribute("minMaxX","sima/hla/Range","",True))
        self.add_attribute(BlueprintAttribute("minMaxY","sima/hla/Range","",True))
        self.add_attribute(Attribute("axisTitleX","string","",default=None))
        self.add_attribute(Attribute("axisTitleY","string","",default=None))
        self.add_attribute(Attribute("valueTypeX","string","",default=None))
        self.add_attribute(Attribute("showTimeMarker","boolean","",default=False))
        self.add_attribute(Attribute("fadePrecedingCurves","boolean","",default=False))
        self.add_attribute(Attribute("fadePrecedingCurvesCount","integer","",default=5))
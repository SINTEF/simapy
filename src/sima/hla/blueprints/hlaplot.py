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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("curves","string","",Dimension("size",""),default=""))
        self.attributes.append(Attribute("crossPlotXAxisValues","string","",default=""))
        self.attributes.append(BlueprintAttribute("minMaxX","sima/hla/Range","",True))
        self.attributes.append(BlueprintAttribute("minMaxY","sima/hla/Range","",True))
        self.attributes.append(Attribute("axisTitleX","string","",default=""))
        self.attributes.append(Attribute("axisTitleY","string","",default=""))
        self.attributes.append(Attribute("valueTypeX","string","",default=""))
        self.attributes.append(Attribute("showTimeMarker","boolean","",default=False))
        self.attributes.append(Attribute("fadePrecedingCurves","boolean","",default=False))
        self.attributes.append(Attribute("fadePrecedingCurvesCount","integer","",default=5))
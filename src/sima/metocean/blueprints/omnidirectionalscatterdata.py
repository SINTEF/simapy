# 
# Generated with OmniDirectionalScatterDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .scatterdata import ScatterDataBlueprint

class OmniDirectionalScatterDataBlueprint(ScatterDataBlueprint):
    """"""

    def __init__(self, name="OmniDirectionalScatterData", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("hsUpperLimits","sima/metocean/ScatterDimension","",True))
        self.add_attribute(BlueprintAttribute("tpUpperLimits","sima/metocean/ScatterDimension","",True))
        self.add_attribute(BlueprintAttribute("windScatter","sima/metocean/ScatterLevelContainer","",True))
        self.add_attribute(BlueprintAttribute("currentScatter","sima/metocean/ScatterLevelContainer","",True))
        self.add_attribute(Attribute("occurrences","integer","",Dimension("*"),default=0))
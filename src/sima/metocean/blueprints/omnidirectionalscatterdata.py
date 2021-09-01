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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("hsUpperLimits","sima/metocean/ScatterDimension","",True))
        self.attributes.append(BlueprintAttribute("tpUpperLimits","sima/metocean/ScatterDimension","",True))
        self.attributes.append(BlueprintAttribute("windScatter","sima/metocean/ScatterLevelContainer","",True))
        self.attributes.append(BlueprintAttribute("currentScatter","sima/metocean/ScatterLevelContainer","",True))
        self.attributes.append(Attribute("occurrences","integer","",Dimension("size",""),default=0))
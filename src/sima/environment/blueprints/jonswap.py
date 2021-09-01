# 
# Generated with JonswapBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wave import WaveBlueprint

class JonswapBlueprint(WaveBlueprint):
    """"""

    def __init__(self, name="Jonswap", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("direction","number","Average wave propagation direction",default=0.0))
        self.attributes.append(Attribute("spreadingExponent","number","Exponent  η in cos spreading function",default=2.0))
        self.attributes.append(Attribute("numDirections","integer","Number of directions in spreading function, must be odd",default=11))
        self.attributes.append(EnumAttribute("spreadingType","sima/environment/WaveSpreadingType","Wave spreading code"))
        self.attributes.append(Attribute("significantWaveHeight","number","Significant wave height",default=0.0))
        self.attributes.append(Attribute("peakPeriod","number","Peak period, Tp",default=0.0))
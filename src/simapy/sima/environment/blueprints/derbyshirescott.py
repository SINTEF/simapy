# 
# Generated with DerbyshireScottBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wave import WaveBlueprint

class DerbyshireScottBlueprint(WaveBlueprint):
    """"""

    def __init__(self, name="DerbyshireScott", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Average wave propagation direction",default=0.0))
        self.add_attribute(Attribute("spreadingExponent","number","Exponent  η in cos spreading function",default=2.0))
        self.add_attribute(Attribute("numDirections","integer","Number of directions in spreading function, must be odd",default=11))
        self.add_attribute(EnumAttribute("spreadingType","sima/environment/WaveSpreadingType","Wave spreading code"))
        self.add_attribute(Attribute("spectrumA","number","Spectrum parameter, a",default=0.214))
        self.add_attribute(Attribute("spectrumB","number","Spectrum parameter, b",default=0.065))
        self.add_attribute(Attribute("spectrumD","number","Spectrum parameter, d",default=0.26))
        self.add_attribute(Attribute("waveHeight","number","Significant wave height",default=0.0))
        self.add_attribute(Attribute("wavePeriod","number","Average wave period",default=0.0))
        self.add_attribute(Attribute("lowerTrunc","number","Lower truncation parameter",default=0.0414))
        self.add_attribute(Attribute("upperTrunc","number","Upper truncation parameter",default=10.367))
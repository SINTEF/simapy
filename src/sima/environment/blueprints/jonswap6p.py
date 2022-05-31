# 
# Generated with Jonswap6PBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wave import WaveBlueprint

class Jonswap6PBlueprint(WaveBlueprint):
    """"""

    def __init__(self, name="Jonswap6P", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("direction","number","Average wave propagation direction",default=0.0))
        self.attributes.append(Attribute("spreadingExponent","number","Exponent  η in cos spreading function",default=2.0))
        self.attributes.append(Attribute("numDirections","integer","Number of directions in spreading function, must be odd",default=11))
        self.attributes.append(EnumAttribute("spreadingType","sima/environment/WaveSpreadingType","Wave spreading code"))
        self.attributes.append(Attribute("omega","number","Peak frequency, ωp",default=0.0))
        self.attributes.append(Attribute("alpha","number","Spectrum parameter α",default=0.008))
        self.attributes.append(Attribute("beta","number","Form parameter, β",default=1.25))
        self.attributes.append(Attribute("gamma","number","Peakedness parameter, γ",default=3.3))
        self.attributes.append(Attribute("sigmaa","number","Spectrum parameter σa",default=0.07))
        self.attributes.append(Attribute("sigmab","number","Spectrum parameter σb",default=0.09))
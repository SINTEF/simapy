# 
# Generated with BretschneiderTwoBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wave import WaveBlueprint

class BretschneiderTwoBlueprint(WaveBlueprint):
    """"""

    def __init__(self, name="BretschneiderTwo", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("direction","number","Average wave propagation direction",default=0.0))
        self.attributes.append(Attribute("spreadingExponent","number","Exponent  η in cos spreading function",default=2.0))
        self.attributes.append(Attribute("numDirections","integer","Number of directions in spreading function, must be odd",default=11))
        self.attributes.append(EnumAttribute("spreadingType","sima/environment/WaveSpreadingType","Wave spreading code"))
        self.attributes.append(Attribute("waveHeight","number","Significant wave height",default=0.0))
        self.attributes.append(Attribute("period","number","Significant wave period",default=0.0))
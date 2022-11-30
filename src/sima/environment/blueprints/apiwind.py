# 
# Generated with APIWindBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class APIWindBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="APIWind", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("frequencyParameter","number","Frequency parameter",default=0.025))
        self.add_attribute(Attribute("layerThickness","number","Surface Layer Thickness",default=20.0))
        self.add_attribute(Attribute("profileExponent","number","Wind profile exponent",default=0.125))
        self.add_attribute(Attribute("averageVelocity","number","Average velocity at reference height",default=0.0))
        self.add_attribute(Attribute("friction","number","Surface drag coefficient.\nAlso used for transverse gust spectrum, if specified in DYNMOD.",default=0.002))
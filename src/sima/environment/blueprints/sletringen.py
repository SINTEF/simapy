# 
# Generated with SletringenBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class SletringenBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="Sletringen", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("profileExponent","number","Wind profile exponent",default=0.11))
        self.add_attribute(Attribute("averageVelocity","number","Average velocity at reference height",default=0.0))
        self.add_attribute(Attribute("friction","number","Surface drag coefficient.\nAlso used for transverse gust spectrum, if specified in DYNMOD.",default=0.002))
        self.add_attribute(Attribute("gamma","number","Temperature stability parameter",default=10.0))
        self.add_attribute(Attribute("referenceHeight","number","Reference height for wind velocity",default=10.0))
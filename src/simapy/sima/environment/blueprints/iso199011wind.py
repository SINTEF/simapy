# 
# Generated with ISO199011WindBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class ISO199011WindBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="ISO199011Wind", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("averageVelocity","number","Average velocity at reference height",default=0.0))
        self.add_attribute(Attribute("profileExponent","number","Wind profile exponent",default=0.11))
        self.add_attribute(Attribute("friction","number","Surface drag coefficient.\nAlso used for transverse gust spectrum, if specified.",default=0.002))
        self.add_attribute(Attribute("referenceHeight","number","Reference height for wind velocity, fixed = 10 m.",default=10.0))
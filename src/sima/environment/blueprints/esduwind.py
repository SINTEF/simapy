# 
# Generated with ESDUWindBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wind import WindBlueprint

class ESDUWindBlueprint(WindBlueprint):
    """"""

    def __init__(self, name="ESDUWind", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Wind propagation direction",default=0.0))
        self.add_attribute(Attribute("averageVelocity","number","Average velocity at reference height",default=0.0))
        self.add_attribute(Attribute("psi","number","Site latitude in decimal degrees",default=0.0))
        self.add_attribute(Attribute("friction","number","Surface drag coefficient used for transverse gust spectrum",default=0.002))
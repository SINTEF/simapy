# 
# Generated with GuidePointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simobodypoint import SIMOBodyPointBlueprint

class GuidePointBlueprint(SIMOBodyPointBlueprint):
    """"""

    def __init__(self, name="GuidePoint", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("winch","sima/simo/Winch","",True))
        self.add_attribute(BlueprintAttribute("tensioner","sima/simo/SIMOTensioner","",True))
        self.add_attribute(BlueprintAttribute("heaveCompensator","sima/simo/SIMOHeaveCompensator","",True))
        self.add_attribute(Attribute("x","number","Local  x position",default=0.0))
        self.add_attribute(Attribute("y","number","Local  y position",default=0.0))
        self.add_attribute(Attribute("z","number","Local z position",default=0.0))
        self.add_attribute(Attribute("diameter","number","Diameter of guide hole",default=0.0))
        self.add_attribute(BlueprintAttribute("normalVector","sima/sima/Vector3","Vector normal to hole in body fixed coordinate system",True))
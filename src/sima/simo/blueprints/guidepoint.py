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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("winch","sima/simo/Winch","",True))
        self.attributes.append(BlueprintAttribute("tensioner","sima/simo/SIMOTensioner","",True))
        self.attributes.append(BlueprintAttribute("heaveCompensator","sima/simo/SIMOHeaveCompensator","",True))
        self.attributes.append(Attribute("x","number","Local  x position",default=0.0))
        self.attributes.append(Attribute("y","number","Local  y position",default=0.0))
        self.attributes.append(Attribute("z","number","Local z position",default=0.0))
        self.attributes.append(Attribute("diameter","number","Diameter of guide hole",default=0.0))
        self.attributes.append(BlueprintAttribute("normalVector","sima/sima/Vector3","Vector normal to hole in body fixed coordinate system",True))
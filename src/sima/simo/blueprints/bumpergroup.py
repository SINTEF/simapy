# 
# Generated with BumperGroupBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class BumperGroupBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="BumperGroup", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("body1","sima/simo/SIMOBody","",False))
        self.add_attribute(BlueprintAttribute("body2","sima/simo/SIMOBody","",False))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.add_attribute(BlueprintAttribute("body1Bumpers","sima/simo/BumperPart","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("body2Bumpers","sima/simo/BumperPart","",True,Dimension("*")))
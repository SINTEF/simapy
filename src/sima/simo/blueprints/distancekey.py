# 
# Generated with DistanceKeyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DistanceKeyBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DistanceKey", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("horisontalDistance","sima/simo/Distance","",False))
        self.add_attribute(BlueprintAttribute("verticalDistance","sima/simo/Distance","",False))
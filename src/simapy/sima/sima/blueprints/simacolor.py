# 
# Generated with SIMAColorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class SIMAColorBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIMAColor", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("red","number","",default=1.0))
        self.add_attribute(Attribute("green","number","",default=0.0))
        self.add_attribute(Attribute("blue","number","",default=0.0))
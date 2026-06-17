# 
# Generated with CurvedPlateProfileItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class CurvedPlateProfileItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CurvedPlateProfileItem", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("distanceAlongAxis","number","",default=0.0))
        self.add_attribute(Attribute("diameter","number","",default=0.0))
# 
# Generated with PositionComparisonBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PositionComparisonBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PositionComparison", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("first","sima/sima/Position","",False))
        self.add_attribute(BlueprintAttribute("second","sima/sima/Position","",False))
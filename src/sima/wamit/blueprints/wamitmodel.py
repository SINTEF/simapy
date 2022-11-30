# 
# Generated with WamitModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WamitModelBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WamitModel", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("environments","sima/wamit/WamitEnvironment","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("location","sima/wamit/WamitLocation","",True))
        self.add_attribute(BlueprintAttribute("bodies","sima/wamit/WamitBody","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("calculationParameters","sima/wamit/WamitCalculationParameters","",True))
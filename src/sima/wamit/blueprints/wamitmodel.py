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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("environments","sima/wamit/WamitEnvironment","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("location","sima/wamit/WamitLocation","",True))
        self.attributes.append(BlueprintAttribute("bodies","sima/wamit/WamitBody","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("calculationParameters","sima/wamit/WamitCalculationParameters","",True))
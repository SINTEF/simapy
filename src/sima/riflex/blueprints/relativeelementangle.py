# 
# Generated with RelativeElementAngleBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RelativeElementAngleBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RelativeElementAngle", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("firstElement","sima/riflex/ElementReference","",True))
        self.add_attribute(BlueprintAttribute("secondElement","sima/riflex/ElementReference","",True))
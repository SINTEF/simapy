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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("firstElement","sima/riflex/ElementReference","",True))
        self.attributes.append(BlueprintAttribute("secondElement","sima/riflex/ElementReference","",True))
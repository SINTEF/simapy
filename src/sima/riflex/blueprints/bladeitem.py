# 
# Generated with BladeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BladeItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BladeItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("eccentricityLine","sima/riflex/ARLine","",False))
        self.attributes.append(BlueprintAttribute("bladeLine","sima/riflex/ARLine","",False))
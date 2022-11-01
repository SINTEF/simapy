# 
# Generated with ForceItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ForceItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ForceItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("distance","number","i'th vertical position in the force vs. vertical position table, (L) For NFZ=1, ZBUOY is dummy, but must be given",default=0.0))
        self.attributes.append(Attribute("force","number","Corresponding vertical force, positive upwards, (F)",default=0.0))
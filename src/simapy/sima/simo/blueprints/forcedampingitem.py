# 
# Generated with ForceDampingItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .forceitem import ForceItemBlueprint

class ForceDampingItemBlueprint(ForceItemBlueprint):
    """"""

    def __init__(self, name="ForceDampingItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("distance","number","i'th vertical position in the force vs. vertical position table, (L) For NFZ=1, ZBUOY is dummy, but must be given",default=0.0))
        self.add_attribute(Attribute("force","number","Corresponding vertical force, positive upwards, (F)",default=0.0))
        self.add_attribute(Attribute("damping","number","Damping coefficient",default=0.0))
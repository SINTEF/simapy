# 
# Generated with ElongationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ElongationItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ElongationItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("strain","number","Relative elongation of segment.",default=0.0))
        self.add_attribute(Attribute("value","number","Stress or tension in segment.",default=0.0))
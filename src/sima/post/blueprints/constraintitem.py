# 
# Generated with ConstraintItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ConstraintItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ConstraintItem", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(EnumAttribute("_type","sima/post/ConstraintType",""))
        self.add_attribute(Attribute("value","number","",default=0.0))
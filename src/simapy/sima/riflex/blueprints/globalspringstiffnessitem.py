# 
# Generated with GlobalSpringStiffnessItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class GlobalSpringStiffnessItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GlobalSpringStiffnessItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("force","number","",default=0.0))
        self.add_attribute(Attribute("displacement","number","",default=0.0))
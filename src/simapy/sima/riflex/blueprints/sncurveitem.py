# 
# Generated with SNCurveItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class SNCurveItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SNCurveItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("slope","number","Slope of curve segment",default=0.0))
        self.add_attribute(Attribute("transitionPoint","number","Transition point between curve segment (i-1) and i - logN",default=0.0))
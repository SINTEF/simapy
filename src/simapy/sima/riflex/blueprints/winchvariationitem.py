# 
# Generated with WinchVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class WinchVariationItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WinchVariationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("winch","sima/riflex/ARWinch","",False))
        self.add_attribute(Attribute("length","number","The length to winch in (-) or out (+)",default=0.0))
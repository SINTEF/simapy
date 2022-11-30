# 
# Generated with BendingStiffnessY_ItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BendingStiffnessY_ItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BendingStiffnessY_Item", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("curvatureValue","number","Curvature value for which bending moment is specified",default=0.0))
        self.add_attribute(Attribute("bendingMoment","number","Corresponding bending moment",default=0.0))
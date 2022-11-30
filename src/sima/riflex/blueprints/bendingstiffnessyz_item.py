# 
# Generated with BendingStiffnessYZ_ItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BendingStiffnessYZ_ItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BendingStiffnessYZ_Item", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("curvatureValue","number","Curvature value for which bending moment is specified",default=0.0))
        self.add_attribute(Attribute("bendingMomentY","number","Bending moment around y-axis corresponding to curvature values.",default=0.0))
        self.add_attribute(Attribute("bendingMomentZ","number","Bending moment around z-axis corresponding to curvature values.",default=0.0))
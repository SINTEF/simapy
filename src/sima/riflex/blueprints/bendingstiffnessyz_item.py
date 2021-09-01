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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("curvatureValue","number","Curvature value for which bending moment is specified",default=0.0))
        self.attributes.append(Attribute("bendingMomentY","number","Bending moment around y-axis corresponding to curvature values.",default=0.0))
        self.attributes.append(Attribute("bendingMomentZ","number","Bending moment around z-axis corresponding to curvature values.",default=0.0))
# 
# Generated with StrainStressItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class StrainStressItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StrainStressItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("strain","number","Strain for a given point on strain-stress curve.",default=0.0))
        self.add_attribute(Attribute("stress","number","Stress for a given point on strain-stress curve.",default=0.0))
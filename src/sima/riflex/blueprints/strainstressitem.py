# 
# Generated with StrainStressItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StrainStressItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StrainStressItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("strain","number","Strain for a given point on strain-stress curve.",default=0.0))
        self.attributes.append(Attribute("stress","number","Stress for a given point on strain-stress curve.",default=0.0))
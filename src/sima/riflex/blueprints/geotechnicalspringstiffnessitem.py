# 
# Generated with GeotechnicalSpringStiffnessItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class GeotechnicalSpringStiffnessItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GeotechnicalSpringStiffnessItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("force","number","Force corresponding to displacement",default=0.0))
        self.attributes.append(Attribute("displacement","number","Spring displacement.",default=0.0))
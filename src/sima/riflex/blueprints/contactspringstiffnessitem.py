# 
# Generated with ContactSpringStiffnessItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ContactSpringStiffnessItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ContactSpringStiffnessItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("force","number","Pressure force per unit length",default=0.0))
        self.attributes.append(Attribute("compression","number","Spring compression",default=0.0))
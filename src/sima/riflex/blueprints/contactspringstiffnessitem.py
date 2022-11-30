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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("force","number","Pressure force per unit length",default=0.0))
        self.add_attribute(Attribute("compression","number","Spring compression",default=0.0))
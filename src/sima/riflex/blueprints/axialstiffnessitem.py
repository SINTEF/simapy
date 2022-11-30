# 
# Generated with AxialStiffnessItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AxialStiffnessItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AxialStiffnessItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("axialForce","number","Axial force corresponding to relative elongation.",default=0.0))
        self.add_attribute(Attribute("relativeElongation","number","Relative elongation",default=0.0))
# 
# Generated with DampingDisplacementItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DampingDisplacementItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DampingDisplacementItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("dampingCoefficient","number","Damping coefficient.",default=0.0))
        self.add_attribute(Attribute("displacement","number","Spring displacement.",default=0.0))
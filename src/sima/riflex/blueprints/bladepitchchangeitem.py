# 
# Generated with BladePitchChangeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BladePitchChangeItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BladePitchChangeItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("rate","number","",default=0.0))
        self.add_attribute(Attribute("maximumPitchAngle","number","Maximum pitch at this rate of pitch change",default=0.0))
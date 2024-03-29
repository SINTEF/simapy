# 
# Generated with GainSchedulingItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class GainSchedulingItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GainSchedulingItem", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("rotorSpeed","number","Rotor speed",default=0.0))
        self.add_attribute(Attribute("gainCorrectionFactor","number","Gain correction factor",default=0.0))
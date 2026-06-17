# 
# Generated with DensityLevelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class DensityLevelBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DensityLevel", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("depth","number","Water depth",default=0.0))
        self.add_attribute(Attribute("waterDensity","number","Water density at this level",default=0.0))
# 
# Generated with DynamicCurrentVariationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynamicCurrentVariationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynamicCurrentVariation", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("active","boolean","",default=False))
        self.add_attribute(Attribute("fileName","string","File name for dynamic current variation"))
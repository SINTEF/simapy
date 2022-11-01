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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("active","boolean","",default=True))
        self.attributes.append(Attribute("fileName","string","File name for dynamic current variation",default=""))
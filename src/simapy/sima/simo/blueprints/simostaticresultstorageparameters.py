# 
# Generated with SIMOStaticResultStorageParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class SIMOStaticResultStorageParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIMOStaticResultStorageParameters", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("storeCatenaryLinesResults","boolean","Store results for Catenary lines?",default=False))
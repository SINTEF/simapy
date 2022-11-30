# 
# Generated with EquilibriumGridDefinitionRowBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class EquilibriumGridDefinitionRowBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EquilibriumGridDefinitionRow", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("minimumValue","number","",default=-10.0))
        self.add_attribute(Attribute("maximumValue","number","",default=10.0))
        self.add_attribute(Attribute("numberOfValues","integer","",default=11))
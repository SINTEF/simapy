# 
# Generated with EquilibriumGridDefinitionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class EquilibriumGridDefinitionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EquilibriumGridDefinition", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("roll","sima/simo/EquilibriumGridDefinitionRow","",True))
        self.add_attribute(BlueprintAttribute("pitch","sima/simo/EquilibriumGridDefinitionRow","",True))
        self.add_attribute(BlueprintAttribute("body","sima/simo/SIMOBody","Body for which the grid will be defined",False))
        self.add_attribute(EnumAttribute("typeOfGrid","sima/simo/EquilibriumGridType",""))
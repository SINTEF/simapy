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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("roll","sima/simo/EquilibriumGridDefinitionRow","",True))
        self.attributes.append(BlueprintAttribute("pitch","sima/simo/EquilibriumGridDefinitionRow","",True))
        self.attributes.append(BlueprintAttribute("body","sima/simo/SIMOBody","Body for which the grid will be defined",False))
        self.attributes.append(EnumAttribute("typeOfGrid","sima/simo/EquilibriumGridType",""))
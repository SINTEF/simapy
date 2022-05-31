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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("minimumValue","number","",default=-10.0))
        self.attributes.append(Attribute("maximumValue","number","",default=10.0))
        self.attributes.append(Attribute("numberOfValues","integer","",default=11))
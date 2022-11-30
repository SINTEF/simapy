# 
# Generated with FrequencyRangeDefinitionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FrequencyRangeDefinitionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FrequencyRangeDefinition", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("fromPeriod","number","",default=0.0))
        self.add_attribute(Attribute("toPeriod","number","",default=0.0))
        self.add_attribute(Attribute("numberOfPeriods","integer","",default=0))
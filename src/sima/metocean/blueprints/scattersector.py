# 
# Generated with ScatterSectorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ScatterSectorBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ScatterSector", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hsUpperLimits","sima/metocean/ScatterDimension","",True))
        self.add_attribute(BlueprintAttribute("tpUpperLimits","sima/metocean/ScatterDimension","",True))
        self.add_attribute(BlueprintAttribute("windScatter","sima/metocean/ScatterLevelContainer","",True))
        self.add_attribute(BlueprintAttribute("currentScatter","sima/metocean/ScatterLevelContainer","",True))
        self.add_attribute(Attribute("occurrences","integer","",Dimension("*"),default=0))
        self.add_attribute(Attribute("direction","number","",default=0.0))
# 
# Generated with SignificantWaveHeightWeibullDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SignificantWaveHeightWeibullDataBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SignificantWaveHeightWeibullData", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("duration","number","",default=0.0))
        self.add_attribute(Attribute("probability","number","",default=0.0))
        self.add_attribute(Attribute("shape","number","",default=0.0))
        self.add_attribute(Attribute("scale","number","",default=0.0))
        self.add_attribute(Attribute("location","number","",default=0.0))
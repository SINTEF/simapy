# 
# Generated with TurbulenceBoxScalingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TurbulenceBoxScalingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TurbulenceBoxScaling", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("scalingOption","sima/windpark/ScalingOption",""))
        self.add_attribute(Attribute("windDirectionScalingFactor","number","",default=1.0))
        self.add_attribute(Attribute("transverseDirectionScalingFactor","number","",default=0.8))
        self.add_attribute(Attribute("verticalDirectionScalingFactor","number","",default=0.5))
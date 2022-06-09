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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("scalingOption","sima/windpark/ScalingOption",""))
        self.attributes.append(Attribute("windDirectionScalingFactor","number","",default=1.0))
        self.attributes.append(Attribute("transverseDirectionScalingFactor","number","",default=0.8))
        self.attributes.append(Attribute("verticalDirectionScalingFactor","number","",default=0.5))
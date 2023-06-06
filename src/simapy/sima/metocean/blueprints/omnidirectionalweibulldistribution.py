# 
# Generated with OmniDirectionalWeibullDistributionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .weibulldistribution import WeibullDistributionBlueprint

class OmniDirectionalWeibullDistributionBlueprint(WeibullDistributionBlueprint):
    """"""

    def __init__(self, name="OmniDirectionalWeibullDistribution", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("returnPeriod","number","",default=0.0))
        self.add_attribute(Attribute("level","number","",default=0.0))
        self.add_attribute(Attribute("duration","number","",default=0.0))
        self.add_attribute(Attribute("probability","number","",default=0.0))
        self.add_attribute(Attribute("shape","number","",default=0.0))
        self.add_attribute(Attribute("scale","number","",default=0.0))
        self.add_attribute(Attribute("location","number","",default=0.0))
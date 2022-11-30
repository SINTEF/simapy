# 
# Generated with HawserForceMeasurementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class HawserForceMeasurementBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="HawserForceMeasurement", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("standardDeviation","number","White noise standard deviation of the measurement system",default=0.0))
        self.add_attribute(Attribute("seed","integer","Seed number for the realisation of the white noise",default=1))
        self.add_attribute(BlueprintAttribute("coupling","sima/simo/SimpleCoupling","",False))
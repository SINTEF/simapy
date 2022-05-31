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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("standardDeviation","number","White noise standard deviation of the measurement system",default=0.0))
        self.attributes.append(Attribute("seed","integer","Seed number for the realisation of the white noise",default=1))
        self.attributes.append(BlueprintAttribute("coupling","sima/simo/SimpleCoupling","",False))
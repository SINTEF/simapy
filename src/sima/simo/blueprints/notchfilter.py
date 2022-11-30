# 
# Generated with NotchFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .estimator import EstimatorBlueprint

class NotchFilterBlueprint(EstimatorBlueprint):
    """"""

    def __init__(self, name="NotchFilter", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("centerPeriod","number","Center period of wave filter",default=10.0))
        self.add_attribute(Attribute("strength","number","Strength of wave filter, between 0 and 1",default=1.0))
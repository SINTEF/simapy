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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("centerPeriod","number","Center period of wave filter",default=10.0))
        self.attributes.append(Attribute("strength","number","Strength of wave filter, between 0 and 1",default=1.0))
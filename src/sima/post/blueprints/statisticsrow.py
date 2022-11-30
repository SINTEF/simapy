# 
# Generated with StatisticsRowBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StatisticsRowBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StatisticsRow", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("unit","string",""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("min","number","",default=0.0))
        self.add_attribute(Attribute("max","number","",default=0.0))
        self.add_attribute(Attribute("mean","number","",default=0.0))
        self.add_attribute(Attribute("standardDeviation","number","",default=0.0))
        self.add_attribute(Attribute("skewness","number","",default=0.0))
        self.add_attribute(Attribute("kurtosis","number","",default=0.0))
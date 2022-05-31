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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("unit","string","",default=""))
        self.attributes.append(Attribute("min","number","",default=0.0))
        self.attributes.append(Attribute("max","number","",default=0.0))
        self.attributes.append(Attribute("mean","number","",default=0.0))
        self.attributes.append(Attribute("standardDeviation","number","",default=0.0))
        self.attributes.append(Attribute("skewness","number","",default=0.0))
        self.attributes.append(Attribute("kurtosis","number","",default=0.0))
# 
# Generated with PerformanceRelationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PerformanceRelationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PerformanceRelation", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("windSpeed","number","",default=0.0))
        self.add_attribute(Attribute("rotorSpeed","number","",default=0.0))
        self.add_attribute(Attribute("bladePitch","number","",default=0.0))
        self.add_attribute(Attribute("power","number","",default=0.0))
        self.add_attribute(Attribute("thrust","number","",default=0.0))
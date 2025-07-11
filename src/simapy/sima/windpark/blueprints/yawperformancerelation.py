# 
# Generated with YawPerformanceRelationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class YawPerformanceRelationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="YawPerformanceRelation", package_path="sima/windpark", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("yawAngle","number","Yaw misalignment",default=0.0))
        self.add_attribute(BlueprintAttribute("items","sima/windpark/PerformanceRelationItem","",True,Dimension("*")))
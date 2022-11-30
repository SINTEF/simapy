# 
# Generated with PeriodEigenvalueResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PeriodEigenvalueResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PeriodEigenvalueResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("period","number","Natural period",default=0.0))
        self.add_attribute(Attribute("surge","number","Value in surge ",default=0.0))
        self.add_attribute(Attribute("sway","number","Value in sway",default=0.0))
        self.add_attribute(Attribute("heave","number","Value in heave",default=0.0))
        self.add_attribute(Attribute("roll","number","Value in roll",default=0.0))
        self.add_attribute(Attribute("pitch","number","Value in pitch",default=0.0))
        self.add_attribute(Attribute("yaw","number","Value in yaw",default=0.0))
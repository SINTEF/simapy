# 
# Generated with BodyEigenvalueResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BodyEigenvalueResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BodyEigenvalueResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("body","string","Result body"))
        self.add_attribute(Attribute("surgeExcursion","number","Excursion in surge",default=0.0))
        self.add_attribute(Attribute("swayExcursion","number","Excursion in sway",default=0.0))
        self.add_attribute(Attribute("heaveExcursion","number","Excursion in heave",default=0.0))
        self.add_attribute(Attribute("rollExcursion","number","Excursion in roll",default=0.0))
        self.add_attribute(Attribute("pitchExcursion","number","Excursion in pitch",default=0.0))
        self.add_attribute(Attribute("yawExcursion","number","Excursion in yaw",default=0.0))
        self.add_attribute(BlueprintAttribute("periodResults","sima/simo/PeriodEigenvalueResult","",True,Dimension("*")))
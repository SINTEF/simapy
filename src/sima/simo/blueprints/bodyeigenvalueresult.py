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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("body","string","Result body",default=""))
        self.attributes.append(Attribute("surgeExcursion","number","Excursion in surge",default=0.0))
        self.attributes.append(Attribute("swayExcursion","number","Excursion in sway",default=0.0))
        self.attributes.append(Attribute("heaveExcursion","number","Excursion in heave",default=0.0))
        self.attributes.append(Attribute("rollExcursion","number","Excursion in roll",default=0.0))
        self.attributes.append(Attribute("pitchExcursion","number","Excursion in pitch",default=0.0))
        self.attributes.append(Attribute("yawExcursion","number","Excursion in yaw",default=0.0))
        self.attributes.append(BlueprintAttribute("periodResults","sima/simo/PeriodEigenvalueResult","",True,Dimension("size","")))
# 
# Generated with BodyEigenvalueItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BodyEigenvalueItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BodyEigenvalueItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("body","sima/simo/SIMOBody","Selected body to compute eigenvalues for",False))
        self.attributes.append(Attribute("surgeExcursion","number","Excursion in surge",default=1.0))
        self.attributes.append(Attribute("swayExcursion","number","Excursion in sway",default=1.0))
        self.attributes.append(Attribute("heaveExcursion","number","Excursion in heave",default=1.0))
        self.attributes.append(Attribute("rollExcursion","number","Excursion in roll",default=1.0))
        self.attributes.append(Attribute("pitchExcursion","number","Excursion in pitch",default=1.0))
        self.attributes.append(Attribute("yawExcursion","number","Excursion in yaw",default=1.0))
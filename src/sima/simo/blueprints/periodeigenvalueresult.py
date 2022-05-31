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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("period","number","Natural period",default=0.0))
        self.attributes.append(Attribute("surge","number","Value in surge ",default=0.0))
        self.attributes.append(Attribute("sway","number","Value in sway",default=0.0))
        self.attributes.append(Attribute("heave","number","Value in heave",default=0.0))
        self.attributes.append(Attribute("roll","number","Value in roll",default=0.0))
        self.attributes.append(Attribute("pitch","number","Value in pitch",default=0.0))
        self.attributes.append(Attribute("yaw","number","Value in yaw",default=0.0))
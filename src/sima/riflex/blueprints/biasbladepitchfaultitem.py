# 
# Generated with BiasBladePitchFaultItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BiasBladePitchFaultItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BiasBladePitchFaultItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("startTime","number","Start time for blade pitch fault",default=0.0))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","",False))
        self.add_attribute(Attribute("pitchDeviation","number","Pitch deviation from required pitch",default=0.0))
        self.add_attribute(Attribute("rampDuration","number","Ramp duration to full pitch deviation",default=0.0))
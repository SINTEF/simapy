# 
# Generated with BladePitchFaultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BladePitchFaultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BladePitchFault", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("seizeFaults","sima/riflex/SeizeBladePitchFaultItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("runawayFaults","sima/riflex/RunawayBladePitchFaultItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("biasFaults","sima/riflex/BiasBladePitchFaultItem","",True,Dimension("*")))
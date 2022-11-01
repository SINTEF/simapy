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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("seizeFaults","sima/riflex/SeizeBladePitchFaultItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("runawayFaults","sima/riflex/RunawayBladePitchFaultItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("biasFaults","sima/riflex/BiasBladePitchFaultItem","",True,Dimension("*")))
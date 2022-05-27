# 
# Generated with SeizeBladePitchFaultItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SeizeBladePitchFaultItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SeizeBladePitchFaultItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("startTime","number","Start time for blade pitch fault",default=0.0))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","",False))
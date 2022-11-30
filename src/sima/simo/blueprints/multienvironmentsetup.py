# 
# Generated with MultiEnvironmentSetupBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class MultiEnvironmentSetupBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="MultiEnvironmentSetup", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("windWaveLowerFrequency","number","Wind wave lower frequency limit",default=0.1))
        self.add_attribute(Attribute("windWaveUpperFrequency","number","Wind wave upper frequency limit",default=3.0))
        self.add_attribute(Attribute("swellWaveLowerFrequency","number","Swell wave lower frequency limit",default=0.05))
        self.add_attribute(Attribute("swellWaveUpperFrequency","number","Swell wave upper frequency limit",default=2.0))
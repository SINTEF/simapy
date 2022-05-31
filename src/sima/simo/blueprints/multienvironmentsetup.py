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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("windWaveLowerFrequency","number","Wind wave lower frequency limit",default=0.1))
        self.attributes.append(Attribute("windWaveUpperFrequency","number","Wind wave upper frequency limit",default=3.0))
        self.attributes.append(Attribute("swellWaveLowerFrequency","number","Swell wave lower frequency limit",default=0.05))
        self.attributes.append(Attribute("swellWaveUpperFrequency","number","Swell wave upper frequency limit",default=2.0))
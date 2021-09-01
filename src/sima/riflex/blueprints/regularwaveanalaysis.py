# 
# Generated with RegularWaveAnalaysisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RegularWaveAnalaysisBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RegularWaveAnalaysis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("periods","integer","Number of periods for regular wave analysis, referring to wave or motion periods (of first vessel)",default=1))
        self.attributes.append(Attribute("timeSteps","integer","Number of integration time steps per period, recommended value: 50-120",default=80))
        self.attributes.append(Attribute("waveActing","boolean","Whether there is a wave acting or not (in which case motions must be present)",default=True))
        self.attributes.append(EnumAttribute("platformMotion","sima/riflex/PlatformMotion","Platform motion options:"))
# 
# Generated with MultiEnvironmentItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class MultiEnvironmentItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="MultiEnvironmentItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("environment","sima/environment/SingleEnvironment","",False))
        self.add_attribute(Attribute("startingTime","number","Time to begin fading to this environment. Note that the new environment is not fully in effect until startingTime + ramp duration",default=0.0))
        self.add_attribute(Attribute("rampDuration","number","Duration of cosine fading from previous to new environment. It is recommended to use at least 10*peak period for the fade-in duration.",default=0.0))
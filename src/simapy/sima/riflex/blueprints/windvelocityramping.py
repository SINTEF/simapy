# 
# Generated with WindVelocityRampingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class WindVelocityRampingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WindVelocityRamping", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("include","boolean","",default=False))
        self.add_attribute(Attribute("rampStartValue","number","",default=0.0))
        self.add_attribute(Attribute("rampDuration","number","",default=0.0))
        self.add_attribute(Attribute("delayed","boolean","Delay the ramp start to half the ramp duration",default=False))
# 
# Generated with ThrusterFailureSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterFailureSpecificationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterFailureSpecification", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ThrusterFailureMode","Thruster failure mode"))
        self.add_attribute(Attribute("failureTime","number","Time for thruster failure",default=0.0))
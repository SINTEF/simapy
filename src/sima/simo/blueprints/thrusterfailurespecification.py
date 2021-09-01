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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ThrusterFailureMode","Thruster failure mode"))
        self.attributes.append(Attribute("failureTime","number","Time for thruster failure",default=0.0))
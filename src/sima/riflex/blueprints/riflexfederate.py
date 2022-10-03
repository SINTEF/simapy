# 
# Generated with RIFLEXFederateBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.simo.blueprints.simofederate import SIMOFederateBlueprint

class RIFLEXFederateBlueprint(SIMOFederateBlueprint):
    """"""

    def __init__(self, name="RIFLEXFederate", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("timeStep","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("task","sima/condition/ConditionTask","",False))
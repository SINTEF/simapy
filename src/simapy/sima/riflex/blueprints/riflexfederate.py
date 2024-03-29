# 
# Generated with RIFLEXFederateBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...simo.blueprints.simofederate import SIMOFederateBlueprint

class RIFLEXFederateBlueprint(SIMOFederateBlueprint):
    """"""

    def __init__(self, name="RIFLEXFederate", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("timeStep","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("task","sima/condition/ConditionTask","",False))
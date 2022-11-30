# 
# Generated with SIMOFederateBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.hla.blueprints.hlafederate import HLAFederateBlueprint

class SIMOFederateBlueprint(HLAFederateBlueprint):
    """"""

    def __init__(self, name="SIMOFederate", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("timeStep","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("task","sima/condition/ConditionTask","",False))
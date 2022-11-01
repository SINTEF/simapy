# 
# Generated with ThrusterReductionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterReductionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterReduction", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("propellerDirection","number","Direction of propeller axis in body coordinate system",default=0.0))
        self.attributes.append(Attribute("reductionFactor","number","Thrust reduction factor",default=1.0))
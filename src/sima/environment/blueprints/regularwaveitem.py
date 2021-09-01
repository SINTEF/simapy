# 
# Generated with RegularWaveItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RegularWaveItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RegularWaveItem", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("amplitude","number","Wave amplitude",default=0.0))
        self.attributes.append(Attribute("period","number","Wave period",default=0.0))
        self.attributes.append(Attribute("phase","number","Phase angle according to theory manual",default=0.0))
        self.attributes.append(Attribute("direction","number","Wave propagation direction",default=0.0))
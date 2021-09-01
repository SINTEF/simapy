# 
# Generated with FibreRopeMassVolumeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FibreRopeMassVolumeBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FibreRopeMassVolume", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("massCoefficient","number","Mass / unit length",default=0.0))
        self.attributes.append(Attribute("extCrossSectionalArea","number","External cross-sectional area",default=0.0))
        self.attributes.append(Attribute("extContactRadius","number","External contact radius (default = 0.0)",default=0.0))
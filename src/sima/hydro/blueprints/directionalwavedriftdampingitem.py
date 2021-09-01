# 
# Generated with DirectionalWaveDriftDampingItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simplifiedwavedriftdamping import SimplifiedWaveDriftDampingBlueprint

class DirectionalWaveDriftDampingItemBlueprint(SimplifiedWaveDriftDampingBlueprint):
    """"""

    def __init__(self, name="DirectionalWaveDriftDampingItem", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("items","sima/hydro/WaveDriftDampingItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("direction","number","",default=0.0))
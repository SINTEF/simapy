# 
# Generated with ForceDampingCharacteristicBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ForceDampingCharacteristicBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ForceDampingCharacteristic", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("dampingExponent","number","Exponent of velocity in damping term",default=1.0))
        self.attributes.append(EnumAttribute("dampingInterpolation","sima/simo/Interpolation","Interpolation method for damping"))
        self.attributes.append(EnumAttribute("forceInterpolation","sima/simo/Interpolation","Interpolation method for force"))
        self.attributes.append(BlueprintAttribute("items","sima/simo/ForceDampingItem","",True,Dimension("size","")))
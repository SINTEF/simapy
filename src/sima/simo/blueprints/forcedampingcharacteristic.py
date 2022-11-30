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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("dampingExponent","number","Exponent of velocity in damping term",default=1.0))
        self.add_attribute(EnumAttribute("dampingInterpolation","sima/simo/Interpolation","Interpolation method for damping"))
        self.add_attribute(EnumAttribute("forceInterpolation","sima/simo/Interpolation","Interpolation method for force"))
        self.add_attribute(BlueprintAttribute("items","sima/simo/ForceDampingItem","",True,Dimension("*")))
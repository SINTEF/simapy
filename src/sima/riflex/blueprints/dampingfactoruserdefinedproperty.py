# 
# Generated with DampingFactorUserDefinedPropertyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .dampingfactorproperty import DampingFactorPropertyBlueprint

class DampingFactorUserDefinedPropertyBlueprint(DampingFactorPropertyBlueprint):
    """"""

    def __init__(self, name="DampingFactorUserDefinedProperty", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("stillWaterDampingFactor","number","Still water damping factor",default=1.0))
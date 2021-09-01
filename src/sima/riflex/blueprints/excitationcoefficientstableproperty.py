# 
# Generated with ExcitationCoefficientsTablePropertyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .excitationcoefficientsproperty import ExcitationCoefficientsPropertyBlueprint

class ExcitationCoefficientsTablePropertyBlueprint(ExcitationCoefficientsPropertyBlueprint):
    """"""

    def __init__(self, name="ExcitationCoefficientsTableProperty", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("nonDimensionalFrequencyProperties","sima/riflex/ExcitationCoefficientsNonDimensionalFrequencyItem","",True,Dimension("size","")))
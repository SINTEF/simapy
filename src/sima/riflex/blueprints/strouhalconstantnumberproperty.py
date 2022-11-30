# 
# Generated with StrouhalConstantNumberPropertyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .strouhalspecificationproperty import StrouhalSpecificationPropertyBlueprint

class StrouhalConstantNumberPropertyBlueprint(StrouhalSpecificationPropertyBlueprint):
    """"""

    def __init__(self, name="StrouhalConstantNumberProperty", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("fixedStrouhalNumber","number","Fixed Strouhal number",default=0.19))
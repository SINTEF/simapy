# 
# Generated with StrouhalUserDefinedPropertyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .strouhalspecificationproperty import StrouhalSpecificationPropertyBlueprint

class StrouhalUserDefinedPropertyBlueprint(StrouhalSpecificationPropertyBlueprint):
    """"""

    def __init__(self, name="StrouhalUserDefinedProperty", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("reynoldStrouhalProperties","sima/riflex/ReynoldStrouhalNumberItem","",True,Dimension("*")))
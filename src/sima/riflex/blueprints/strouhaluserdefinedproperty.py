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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("reynoldStrouhalProperties","sima/riflex/ReynoldStrouhalNumberItem","",True,Dimension("size","")))
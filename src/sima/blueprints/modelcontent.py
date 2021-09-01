# 
# Generated with ModelContentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ModelContentBlueprint(Blueprint):
    """"""

    def __init__(self, name="ModelContent", package_path="sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("header","sima/Header","",True))
        self.attributes.append(BlueprintAttribute("contents","simasystem/SIMOS/NamedEntity","",True,Dimension("size","")))
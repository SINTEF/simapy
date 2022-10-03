# 
# Generated with HeaderBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class HeaderBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="Header", package_path="sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(BlueprintAttribute("packages","sima/PackageInfo","",True,Dimension("*")))
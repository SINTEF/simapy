# 
# Generated with PackageInfoBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class PackageInfoBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="PackageInfo", package_path="sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("version","integer","",default=0))
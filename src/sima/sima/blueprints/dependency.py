# 
# Generated with DependencyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class DependencyBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="Dependency", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("object","sima/sima/MOAO","",False))
        self.attributes.append(Attribute("feature","string","",default=""))
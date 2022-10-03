# 
# Generated with FontBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class FontBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="Font", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("size","integer","",default=10))
        self.attributes.append(Attribute("font","string","",default=""))
        self.attributes.append(EnumAttribute("style","marmo/report/FontStyle",""))
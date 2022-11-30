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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("size","integer","",default=10))
        self.add_attribute(Attribute("font","string",""))
        self.add_attribute(EnumAttribute("style","marmo/report/FontStyle",""))
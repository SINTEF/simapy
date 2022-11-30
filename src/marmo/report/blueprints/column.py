# 
# Generated with ColumnBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class ColumnBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="Column", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("header","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(BlueprintAttribute("headerfont","marmo/report/Font","",True))
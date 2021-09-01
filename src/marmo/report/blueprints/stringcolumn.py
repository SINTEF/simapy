# 
# Generated with StringColumnBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .column import ColumnBlueprint

class StringColumnBlueprint(ColumnBlueprint):
    """"""

    def __init__(self, name="StringColumn", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("header","string",""))
        self.attributes.append(Attribute("label","string",""))
        self.attributes.append(BlueprintAttribute("headerfont","/report/Font","",True))
        self.attributes.append(Attribute("cells","string","",Dimension("size","")))
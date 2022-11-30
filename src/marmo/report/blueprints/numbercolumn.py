# 
# Generated with NumberColumnBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .column import ColumnBlueprint

class NumberColumnBlueprint(ColumnBlueprint):
    """"""

    def __init__(self, name="NumberColumn", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("header","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(BlueprintAttribute("headerfont","marmo/report/Font","",True))
        self.add_attribute(Attribute("cells","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("format","string",""))
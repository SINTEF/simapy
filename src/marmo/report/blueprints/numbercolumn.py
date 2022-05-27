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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("header","string","",default=""))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(BlueprintAttribute("headerfont","marmo/report/Font","",True))
        self.attributes.append(Attribute("cells","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("format","string","",default=""))
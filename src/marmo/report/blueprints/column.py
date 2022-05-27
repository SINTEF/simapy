# 
# Generated with ColumnBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ColumnBlueprint(Blueprint):
    """"""

    def __init__(self, name="Column", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("header","string","",default=""))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(BlueprintAttribute("headerfont","marmo/report/Font","",True))
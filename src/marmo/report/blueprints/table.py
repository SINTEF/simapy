# 
# Generated with TableBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class TableBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="Table", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("caption","string","",default=""))
        self.attributes.append(Attribute("transposed","boolean","",default=True))
        self.attributes.append(BlueprintAttribute("columns","marmo/report/Column","",True,Dimension("*")))
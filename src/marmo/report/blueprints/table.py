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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("caption","string",""))
        self.add_attribute(Attribute("transposed","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("columns","marmo/report/Column","",True,Dimension("*")))
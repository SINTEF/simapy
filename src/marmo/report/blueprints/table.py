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
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("caption","string",""))
        self.attributes.append(Attribute("transposed","boolean",""))
        self.attributes.append(BlueprintAttribute("columns","/report/Column","",True,Dimension("size","")))
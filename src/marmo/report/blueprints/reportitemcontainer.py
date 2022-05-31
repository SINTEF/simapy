# 
# Generated with ReportItemContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ReportItemContainerBlueprint(Blueprint):
    """"""

    def __init__(self, name="ReportItemContainer", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("items","marmo/report/ReportItem","",True,Dimension("*")))
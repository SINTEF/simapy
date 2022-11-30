# 
# Generated with ReportBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitemcontainer import ReportItemContainerBlueprint

class ReportBlueprint(ReportItemContainerBlueprint):
    """"""

    def __init__(self, name="Report", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("items","marmo/report/ReportItem","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("subtitle","string",""))
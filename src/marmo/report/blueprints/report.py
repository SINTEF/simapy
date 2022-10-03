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
        self.attributes.append(BlueprintAttribute("items","marmo/report/ReportItem","",True,Dimension("*")))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("subtitle","string","",default=""))
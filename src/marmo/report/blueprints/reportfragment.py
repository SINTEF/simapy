# 
# Generated with ReportFragmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitemcontainer import ReportItemContainerBlueprint

class ReportFragmentBlueprint(ReportItemContainerBlueprint):
    """"""

    def __init__(self, name="ReportFragment", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("items","marmo/report/ReportItem","",True,Dimension("*")))
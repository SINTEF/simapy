# 
# Generated with SectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitemcontainer import ReportItemContainerBlueprint
from .reportitem import ReportItemBlueprint

class SectionBlueprint(ReportItemContainerBlueprint,ReportItemBlueprint):
    """"""

    def __init__(self, name="Section", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("items","marmo/report/ReportItem","",True,Dimension("*")))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("landscape","boolean","",default=False))
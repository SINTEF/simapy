# 
# Generated with AppendixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .section import SectionBlueprint

class AppendixBlueprint(SectionBlueprint):
    """"""

    def __init__(self, name="Appendix", package_path="sima/signals/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("items","sima/signals/report/ReportItem","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string","",optional=False))
        self.add_attribute(Attribute("landscape","boolean","",default=False))
        self.add_attribute(Attribute("pageBreakBefore","boolean","",default=False))
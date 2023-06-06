# 
# Generated with ReportSectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportfragmentitemcontainer import ReportFragmentItemContainerBlueprint

class ReportSectionBlueprint(ReportFragmentItemContainerBlueprint):
    """"""

    def __init__(self, name="ReportSection", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("reportFragmentItems","sima/workflow/ReportFragmentItem","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("pageBreakBefore","boolean","",default=False))
        self.add_attribute(EnumAttribute("orientation","sima/report/Orientation",""))
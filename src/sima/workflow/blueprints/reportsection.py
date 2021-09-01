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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("reportFragmentItems","sima/workflow/ReportFragmentItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("pageBreakBefore","boolean","",default=False))
        self.attributes.append(EnumAttribute("orientation","sima/report/Orientation",""))
# 
# Generated with SectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint
from .linkable import LinkableBlueprint

class SectionBlueprint(ReportItemBlueprint,LinkableBlueprint):
    """"""

    def __init__(self, name="Section", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("identifier","string",""))
        self.add_attribute(BlueprintAttribute("items","sima/report/ReportItem","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string","The title of the section."))
        self.add_attribute(Attribute("pageBreakBefore","boolean","",default=False))
        self.add_attribute(EnumAttribute("orientation","sima/report/Orientation",""))
# 
# Generated with AppendixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint
from .linkable import LinkableBlueprint

class AppendixBlueprint(ReportItemBlueprint,LinkableBlueprint):
    """"""

    def __init__(self, name="Appendix", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("identifier","string","",default=""))
        self.attributes.append(BlueprintAttribute("items","sima/report/ReportItem","",True,Dimension("*")))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("pageBreakBefore","boolean","",default=False))
        self.attributes.append(EnumAttribute("orientation","sima/report/Orientation",""))
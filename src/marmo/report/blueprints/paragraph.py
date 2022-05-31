# 
# Generated with ParagraphBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class ParagraphBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="Paragraph", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("text","string","",default=""))
        self.attributes.append(Attribute("markup","boolean","",default=False))
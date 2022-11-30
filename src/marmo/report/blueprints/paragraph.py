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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("text","string",""))
        self.add_attribute(Attribute("markup","boolean","",default=False))
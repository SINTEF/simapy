# 
# Generated with ImageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class ImageBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="Image", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("caption","string",""))
        self.add_attribute(Attribute("height","integer","",default=0))
        self.add_attribute(Attribute("width","integer","",default=0))
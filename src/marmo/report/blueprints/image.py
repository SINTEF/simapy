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
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("path","string",""))
        self.attributes.append(Attribute("caption","string",""))
        self.attributes.append(Attribute("height","integer",""))
        self.attributes.append(Attribute("width","integer",""))
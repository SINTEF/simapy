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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("caption","string","",default=""))
        self.attributes.append(Attribute("height","integer","",default=0))
        self.attributes.append(Attribute("width","integer","",default=0))
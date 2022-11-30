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

    def __init__(self, name="Image", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("caption","string","Caption"))
        self.add_attribute(Attribute("filePath","string","Path to the image"))
        self.add_attribute(Attribute("width","integer","The image witdth in twips (1/1440 inch). If only the width is specified the height will be automatically calculated.",default=0))
        self.add_attribute(Attribute("height","integer","The image height in twips (1/1440 inch). If only the width is specified the height will be automatically calculated.",default=0))
# 
# Generated with TextFileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class TextFileBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="TextFile", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("path","string","Absolute path to the text file to be read in.",default=""))
        self.attributes.append(Attribute("plainText","boolean","Whether or not the text file contains Wiki markup code to be parsed.",default=False))
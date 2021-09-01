# 
# Generated with ReportTextFileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportfragmentitem import ReportFragmentItemBlueprint

class ReportTextFileBlueprint(ReportFragmentItemBlueprint):
    """"""

    def __init__(self, name="ReportTextFile", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("plainText","boolean","",default=False))
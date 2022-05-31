# 
# Generated with ReportRunBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class ReportRunBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="ReportRun", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("tooltip","string","",default=""))
        self.attributes.append(BlueprintAttribute("report","sima/report/Report","",False))
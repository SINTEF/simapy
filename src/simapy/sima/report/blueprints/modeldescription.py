# 
# Generated with ModelDescriptionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class ModelDescriptionBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="ModelDescription", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("object","sima/sima/MOAO","",False))
        self.add_attribute(Attribute("caption","string","Caption"))
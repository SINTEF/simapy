# 
# Generated with ReportFragmentItemContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportfragmentitem import ReportFragmentItemBlueprint

class ReportFragmentItemContainerBlueprint(ReportFragmentItemBlueprint):
    """"""

    def __init__(self, name="ReportFragmentItemContainer", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("reportFragmentItems","sima/workflow/ReportFragmentItem","",True,Dimension("*")))
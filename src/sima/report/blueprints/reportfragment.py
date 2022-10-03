# 
# Generated with ReportFragmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint
from sima.sima.blueprints.named import NamedBlueprint

class ReportFragmentBlueprint(ReportItemBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="ReportFragment", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(BlueprintAttribute("fragment","sima/report/ReportFragmentReference","",False))
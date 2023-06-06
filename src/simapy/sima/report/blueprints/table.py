# 
# Generated with TableBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportitem import ReportItemBlueprint

class TableBlueprint(ReportItemBlueprint):
    """"""

    def __init__(self, name="Table", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("object","sima/sima/MOAO","",False))
        self.add_attribute(Attribute("caption","string","Caption"))
        self.add_attribute(Attribute("autoSplit","boolean","Automatically split a large table into multiple tables.",default=True))
        self.add_attribute(BlueprintAttribute("columns","sima/report/TableColumn","",True,Dimension("*")))
        self.add_attribute(Attribute("customisableTable","boolean","",default=False))
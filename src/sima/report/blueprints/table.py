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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("object","sima/sima/MOAO","",False))
        self.attributes.append(Attribute("caption","string","Caption",default=""))
        self.attributes.append(Attribute("autoSplit","boolean","Automatically split a large table into multiple tables.",default=True))
        self.attributes.append(BlueprintAttribute("columns","sima/report/TableColumn","",True,Dimension("*")))
        self.attributes.append(Attribute("customisableTable","boolean","",default=False))
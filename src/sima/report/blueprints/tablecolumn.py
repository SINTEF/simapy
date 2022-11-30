# 
# Generated with TableColumnBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TableColumnBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TableColumn", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("header","string",""))
        self.add_attribute(BlueprintAttribute("headerStyle","sima/report/TableCellStyle","",True))
        self.add_attribute(BlueprintAttribute("cells","sima/report/TableCell","",True,Dimension("*")))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("header","string","",default=""))
        self.attributes.append(BlueprintAttribute("headerStyle","sima/report/TableCellStyle","",True))
        self.attributes.append(BlueprintAttribute("cells","sima/report/TableCell","",True,Dimension("size","")))
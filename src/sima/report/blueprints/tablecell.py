# 
# Generated with TableCellBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .tablecellstyle import TableCellStyleBlueprint

class TableCellBlueprint(TableCellStyleBlueprint):
    """"""

    def __init__(self, name="TableCell", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("font","sima/sima/FontDescription","",True))
        self.attributes.append(EnumAttribute("horizontalTextAlignment","sima/report/HorizontalAlignment",""))
        self.attributes.append(EnumAttribute("verticalTextAlignment","sima/report/VerticalAlignment",""))
        self.attributes.append(Attribute("value","string","",default=""))
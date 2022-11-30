# 
# Generated with TableCellStyleBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class TableCellStyleBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TableCellStyle", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("font","sima/sima/FontDescription","",True))
        self.add_attribute(EnumAttribute("horizontalTextAlignment","sima/report/HorizontalAlignment",""))
        self.add_attribute(EnumAttribute("verticalTextAlignment","sima/report/VerticalAlignment",""))
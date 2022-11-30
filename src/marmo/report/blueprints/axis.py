# 
# Generated with AxisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class AxisBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="Axis", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("font","marmo/report/Font","",True))
        self.add_attribute(Attribute("log","boolean","",default=False))
        self.add_attribute(Attribute("autoformat","boolean","",default=True))
        self.add_attribute(Attribute("format","string",""))
        self.add_attribute(Attribute("autoscale","boolean","",default=True))
        self.add_attribute(Attribute("showgrid","boolean","",default=True))
        self.add_attribute(Attribute("dashgridline","boolean","",default=True))
# 
# Generated with AxisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class AxisBlueprint(Blueprint):
    """"""

    def __init__(self, name="Axis", package_path="marmo/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("font","marmo/report/Font","",True))
        self.attributes.append(Attribute("log","boolean","",default=True))
        self.attributes.append(Attribute("autoformat","boolean","",default=True))
        self.attributes.append(Attribute("format","string","",default=""))
        self.attributes.append(Attribute("autoscale","boolean","",default=True))
        self.attributes.append(Attribute("showgrid","boolean","",default=True))
        self.attributes.append(Attribute("dashgridline","boolean","",default=True))
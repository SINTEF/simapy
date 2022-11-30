# 
# Generated with ReportBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ReportBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="Report", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("items","sima/report/ReportItem","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string","The title of the report."))
        self.add_attribute(Attribute("subtitle","string","A sub title for the report."))
        self.add_attribute(Attribute("filePath","string","Optional path to the generated report file"))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("items","sima/report/ReportItem","",True,Dimension("*")))
        self.attributes.append(Attribute("title","string","The title of the report.",default=""))
        self.attributes.append(Attribute("subtitle","string","A sub title for the report.",default=""))
        self.attributes.append(Attribute("filePath","string","Optional path to the generated report file",default=""))
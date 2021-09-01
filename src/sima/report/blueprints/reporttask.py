# 
# Generated with ReportTaskBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.task import TaskBlueprint

class ReportTaskBlueprint(TaskBlueprint):
    """"""

    def __init__(self, name="ReportTask", package_path="sima/report", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("size","")))
        self.attributes.append(Attribute("runNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("reports","sima/report/Report","",True,Dimension("size","")))
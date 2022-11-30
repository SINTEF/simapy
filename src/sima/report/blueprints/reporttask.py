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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.add_attribute(Attribute("runNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("reports","sima/report/Report","",True,Dimension("*")))
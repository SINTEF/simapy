# 
# Generated with WorkflowReportFragmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.report.blueprints.reportfragment import ReportFragmentBlueprint

class WorkflowReportFragmentBlueprint(ReportFragmentBlueprint):
    """"""

    def __init__(self, name="WorkflowReportFragment", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("fragment","sima/report/ReportFragmentReference","",False))
        self.add_attribute(BlueprintAttribute("items","sima/report/ReportItem","",True,Dimension("*")))
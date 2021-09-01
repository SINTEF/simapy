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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("fragment","sima/report/ReportFragmentReference","",False))
        self.attributes.append(BlueprintAttribute("items","sima/report/ReportItem","",True,Dimension("size","")))
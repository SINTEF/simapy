# 
# Generated with WorkflowContainerPackageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class WorkflowContainerPackageBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="WorkflowContainerPackage", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("packages","sima/workflow/WorkflowContainerPackage","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("workflows","sima/workflow/Workflow","",True,Dimension("*")))
        self.add_attribute(Attribute("visible","boolean","Make all workflows directly contained in this package visible outside of the task",default=False))
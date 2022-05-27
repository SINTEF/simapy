# 
# Generated with WorkflowContainerPackageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WorkflowContainerPackageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WorkflowContainerPackage", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("packages","sima/workflow/WorkflowContainerPackage","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("workflows","sima/workflow/Workflow","",True,Dimension("*")))
        self.attributes.append(Attribute("visible","boolean","Make all workflows directly contained in this package visible outside of the task",default=False))
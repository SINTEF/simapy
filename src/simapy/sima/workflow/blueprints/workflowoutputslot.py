# 
# Generated with WorkflowOutputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...post.blueprints.outputslot import OutputSlotBlueprint

class WorkflowOutputSlotBlueprint(OutputSlotBlueprint):
    """"""

    def __init__(self, name="WorkflowOutputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("workflowOutput","sima/workflow/WorkflowOutput","",False))
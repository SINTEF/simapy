# 
# Generated with WorkflowInputVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .workflowlinkitem import WorkflowLinkItemBlueprint

class WorkflowInputVariationItemBlueprint(WorkflowLinkItemBlueprint):
    """"""

    def __init__(self, name="WorkflowInputVariationItem", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("fromId","string",""))
        self.add_attribute(Attribute("toId","string",""))
        self.add_attribute(Attribute("runRoots","string","",Dimension("*")))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("fromId","string","",default=""))
        self.attributes.append(Attribute("toId","string","",default=""))
        self.attributes.append(Attribute("runRoots","string","",Dimension("*"),default=""))
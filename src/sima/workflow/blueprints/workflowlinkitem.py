# 
# Generated with WorkflowLinkItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WorkflowLinkItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WorkflowLinkItem", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("fromId","string","",default=""))
        self.attributes.append(Attribute("toId","string","",default=""))
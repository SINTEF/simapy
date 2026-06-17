# 
# Generated with NodeMessageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class NodeMessageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="NodeMessage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("severity","sima/sima/Severity",""))
        self.add_attribute(Attribute("line","string",""))
        self.add_attribute(Attribute("segmentNumber","integer","",default=0))
        self.add_attribute(Attribute("nodeNumber","integer","",default=0))
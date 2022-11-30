# 
# Generated with SimaMessageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class SimaMessageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SimaMessage", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(EnumAttribute("severity","sima/sima/Severity",""))
        self.add_attribute(BlueprintAttribute("messages","sima/sima/SimaMessage","",True,Dimension("*")))
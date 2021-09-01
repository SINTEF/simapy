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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(EnumAttribute("severity","sima/sima/Severity",""))
        self.attributes.append(BlueprintAttribute("messages","sima/sima/SimaMessage","",True,Dimension("size","")))
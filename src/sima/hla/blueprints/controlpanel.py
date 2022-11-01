# 
# Generated with ControlPanelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ControlPanelBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ControlPanel", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("children","sima/custom/CustomComponent","",True,Dimension("*")))
        self.attributes.append(Attribute("title","string","",default=""))
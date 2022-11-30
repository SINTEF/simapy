# 
# Generated with SIMAWorkspaceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class SIMAWorkspaceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIMAWorkspace", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("childFolders","sima/sima/TaskFolder","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("tasks","sima/sima/Task","",True,Dimension("*")))
        self.add_attribute(Attribute("productId","string",""))
        self.add_attribute(Attribute("dateAndTime","string",""))
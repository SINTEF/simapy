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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("childFolders","sima/sima/TaskFolder","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("tasks","sima/sima/Task","",True,Dimension("*")))
        self.attributes.append(Attribute("productId","string","",default=""))
        self.attributes.append(Attribute("dateAndTime","string","",default=""))
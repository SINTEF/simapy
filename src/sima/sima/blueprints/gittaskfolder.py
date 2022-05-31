# 
# Generated with GitTaskFolderBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .taskfolder import TaskFolderBlueprint

class GitTaskFolderBlueprint(TaskFolderBlueprint):
    """"""

    def __init__(self, name="GitTaskFolder", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("childFolders","sima/sima/TaskFolder","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("childTasks","sima/sima/Task","",True,Dimension("*")))
        self.attributes.append(Attribute("visible","boolean","",default=True))
        self.attributes.append(Attribute("remoteURI","string","",default=""))
        self.attributes.append(Attribute("branch","string","",default=""))
        self.attributes.append(Attribute("lastCommitMessage","string","",default=""))
        self.attributes.append(Attribute("repositoryFolder","string","",default=""))
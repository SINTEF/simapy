# 
# Generated with TaskFolderBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .named import NamedBlueprint

class TaskFolderBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="TaskFolder", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("childFolders","sima/sima/TaskFolder","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("childTasks","sima/sima/Task","",True,Dimension("*")))
        self.add_attribute(Attribute("visible","boolean","",default=True))
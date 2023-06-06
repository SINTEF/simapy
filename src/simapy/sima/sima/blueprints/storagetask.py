# 
# Generated with StorageTaskBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .task import TaskBlueprint

class StorageTaskBlueprint(TaskBlueprint):
    """"""

    def __init__(self, name="StorageTask", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.add_attribute(Attribute("runNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/sima/StorageTaskType",""))
        self.add_attribute(Attribute("root","string","Defines the root of the storage task. If not set, the root will be the normal workspace task location"))
        self.add_attribute(Attribute("includeInExport","boolean","If not set the file content withing this storage task will be ommitted when exporting.",default=True))
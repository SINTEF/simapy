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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("size","")))
        self.attributes.append(Attribute("runNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("_type","sima/sima/StorageTaskType",""))
        self.attributes.append(Attribute("root","string","Defines the root of the storage task. If not set, the root will be the normal workspace task location",default=""))
        self.attributes.append(Attribute("includeInExport","boolean","If not set the file content withing this storage task will be ommitted when exporting.",default=True))
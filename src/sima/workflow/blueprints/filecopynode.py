# 
# Generated with FileCopyNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class FileCopyNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="FileCopyNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("size","")))
        self.attributes.append(Attribute("ignoreEmptyInput","boolean","Do not run if input is empty",default=False))
        self.attributes.append(Attribute("folder","boolean","If this is set, all files that er input to the operation will be copied to the destination, otherwise a single file is expected",default=False))
        self.attributes.append(Attribute("path","string","Path to the output file.",default=""))
        self.attributes.append(Attribute("retainStructure","boolean","Retain structure of input",default=False))
        self.attributes.append(Attribute("cleanUpFolder","boolean","Delete all contained files and folders in the given folder before copying",default=False))
        self.attributes.append(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
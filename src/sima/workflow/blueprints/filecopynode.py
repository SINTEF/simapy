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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("ignoreEmptyInput","boolean","Do not run if input is empty",default=False))
        self.add_attribute(Attribute("folder","boolean","If this is set, all files that er input to the operation will be copied to the destination, otherwise a single file is expected",default=False))
        self.add_attribute(Attribute("path","string","Path to the output file."))
        self.add_attribute(Attribute("retainStructure","boolean","Retain structure of input",default=False))
        self.add_attribute(Attribute("cleanUpFolder","boolean","Delete all contained files and folders in the given folder before copying",default=False))
        self.add_attribute(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
# 
# Generated with FileInputSourceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class FileInputSourceBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="FileInputSource", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("filePath","string","Path to the input file."))
        self.add_attribute(Attribute("fileFromInput","boolean","Input the filename to be imported from an input slot",default=False))
        self.add_attribute(EnumAttribute("format","sima/post/FileInputFormat",""))
        self.add_attribute(Attribute("firstIsX","boolean","Use the first signal as the x axis for all inputs",default=False))
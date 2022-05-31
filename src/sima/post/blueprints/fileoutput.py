# 
# Generated with FileOutputBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint
from .outputnode import OutputNodeBlueprint
from .signalpropertiescontainer import SignalPropertiesContainerBlueprint

class FileOutputBlueprint(OperationNodeBlueprint,OutputNodeBlueprint,SignalPropertiesContainerBlueprint):
    """"""

    def __init__(self, name="FileOutput", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("filePath","string","Path to the output file.",default=""))
        self.attributes.append(EnumAttribute("fileFormat","sima/post/FileFormat","Format of the exported file."))
        self.attributes.append(Attribute("shellCommand","string","Shell command to execute after the export.",default=""))
        self.attributes.append(Attribute("addMetaTags","boolean","Include metadata tags in output",default=False))
        self.attributes.append(EnumAttribute("decimalSeparator","sima/post/DecimalSeparator","Set according to the language of Excel. Comma as\ndecimal-separator will make semicolon the value-separator."))
        self.attributes.append(Attribute("skipHeader","boolean","Do not write a header on the file",default=False))
        self.attributes.append(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the file root",default=False))
        self.attributes.append(Attribute("writeRawText","boolean","Writes a single input string into the given file",default=False))
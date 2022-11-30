# 
# Generated with FileOutputNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.outputnode import OutputNodeBlueprint
from sima.post.blueprints.signalpropertiescontainer import SignalPropertiesContainerBlueprint

class FileOutputNodeBlueprint(OutputNodeBlueprint,SignalPropertiesContainerBlueprint):
    """"""

    def __init__(self, name="FileOutputNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.add_attribute(Attribute("filePath","string","Path to the output file."))
        self.add_attribute(EnumAttribute("fileFormat","sima/post/FileFormat","Format of the exported file."))
        self.add_attribute(Attribute("shellCommand","string","Shell command to execute after the export."))
        self.add_attribute(Attribute("addMetaTags","boolean","Include metadata tags in output",default=False))
        self.add_attribute(EnumAttribute("decimalSeparator","sima/post/DecimalSeparator","Set according to the language of Excel. Comma as\ndecimal-separator will make semicolon the value-separator."))
        self.add_attribute(Attribute("skipHeader","boolean","Do not write a header on the file",default=False))
        self.add_attribute(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the file root",default=False))
        self.add_attribute(Attribute("writeRawText","boolean","Writes a single input string into the given file",default=False))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
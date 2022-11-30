# 
# Generated with ExternalProgramNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class ExternalProgramNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="ExternalProgramNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("executable","string","Executable to run"))
        self.add_attribute(Attribute("arguments","string","Process arguments"))
        self.add_attribute(BlueprintAttribute("fileInputSlots","sima/workflow/FileInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("fileOutputSlots","sima/workflow/FileOutputSlot","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("fileFormat","sima/post/FileFormat","file format"))
        self.add_attribute(Attribute("failOnErrorCode","boolean","When checked, the workflow will fail if the external program exits with a non-zero exit code. This is usually the preferred behaviour.",default=True))
        self.add_attribute(Attribute("addInputFiles","boolean","Add additional input files before running. These will be copied to working directory",default=False))
        self.add_attribute(BlueprintAttribute("inputFileSlot","sima/post/InputSlot","",True))
        self.add_attribute(Attribute("environmentVariables","string","Environment variables to set when executing. Separate each variable with a semicolon and path segments with colon."))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("executable","string","Executable to run",default=""))
        self.attributes.append(Attribute("arguments","string","Process arguments",default=""))
        self.attributes.append(BlueprintAttribute("fileInputSlots","sima/workflow/FileInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("fileOutputSlots","sima/workflow/FileOutputSlot","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("fileFormat","sima/post/FileFormat","file format"))
        self.attributes.append(Attribute("failOnErrorCode","boolean","When checked, the workflow will fail if the external program exits with a non-zero exit code. This is usually the preferred behaviour.",default=True))
        self.attributes.append(Attribute("addInputFiles","boolean","Add additional input files before running. These will be copied to working directory",default=False))
        self.attributes.append(BlueprintAttribute("inputFileSlot","sima/post/InputSlot","",True))
        self.attributes.append(Attribute("environmentVariables","string","Environment variables to set when executing. Separate each variable with a semicolon and path segments with colon.",default=""))
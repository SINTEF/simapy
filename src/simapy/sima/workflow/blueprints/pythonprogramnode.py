# 
# Generated with PythonProgramNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...post.blueprints.runnode import RunNodeBlueprint

class PythonProgramNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="PythonProgramNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("file","string","Python program to run",optional=False))
        self.add_attribute(BlueprintAttribute("fileInputSlots","sima/workflow/FileInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("fileOutputSlots","sima/workflow/FileOutputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/SingleValue","",True,Dimension("*")))
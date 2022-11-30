# 
# Generated with FileOutputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.outputslot import OutputSlotBlueprint

class FileOutputSlotBlueprint(OutputSlotBlueprint):
    """"""

    def __init__(self, name="FileOutputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("filename","string","Name of file to be imported"))
        self.add_attribute(Attribute("pathOnly","boolean","Import the path to the specified file and not the content",default=False))
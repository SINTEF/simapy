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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("filename","string","Name of file to be imported",default=""))
        self.attributes.append(Attribute("pathOnly","boolean","Import the path to the specified file and not the content",default=False))
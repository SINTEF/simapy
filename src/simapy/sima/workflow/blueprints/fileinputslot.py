# 
# Generated with FileInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...post.blueprints.inputslot import InputSlotBlueprint
from ...post.blueprints.signalpropertiescontainer import SignalPropertiesContainerBlueprint

class FileInputSlotBlueprint(InputSlotBlueprint,SignalPropertiesContainerBlueprint):
    """"""

    def __init__(self, name="FileInputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("filename","string","Name of file to be imported"))
        self.add_attribute(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the file root",default=False))
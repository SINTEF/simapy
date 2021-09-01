# 
# Generated with FileInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.inputslot import InputSlotBlueprint
from sima.post.blueprints.signalpropertiescontainer import SignalPropertiesContainerBlueprint

class FileInputSlotBlueprint(InputSlotBlueprint,SignalPropertiesContainerBlueprint):
    """"""

    def __init__(self, name="FileInputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("size","")))
        self.attributes.append(Attribute("filename","string","Name of file to be imported",default=""))
        self.attributes.append(Attribute("specifyAdditionalProperties","boolean","Specify additional properties in the file root",default=False))
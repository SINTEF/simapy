# 
# Generated with BodyInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.inputslot import InputSlotBlueprint

class BodyInputSlotBlueprint(InputSlotBlueprint):
    """"""

    def __init__(self, name="BodyInputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("length","number","Length",default=10.0))
        self.attributes.append(Attribute("width","number","Width",default=5.0))
        self.attributes.append(Attribute("height","number","Height",default=5.0))
        self.attributes.append(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
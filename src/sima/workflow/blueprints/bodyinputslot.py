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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("length","number","Length",default=10.0))
        self.add_attribute(Attribute("width","number","Width",default=5.0))
        self.add_attribute(Attribute("height","number","Height",default=5.0))
        self.add_attribute(BlueprintAttribute("appearance","sima/sima/Appearance","",True))
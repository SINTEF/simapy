# 
# Generated with ModelInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.inputslot import InputSlotBlueprint

class ModelInputSlotBlueprint(InputSlotBlueprint):
    """"""

    def __init__(self, name="ModelInputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("reference","sima/sima/ModelReferenceVariable","Model reference to be replaced",False))
        self.add_attribute(Attribute("replaceChildren","boolean","If checked the children of the reference will replaced",default=False))
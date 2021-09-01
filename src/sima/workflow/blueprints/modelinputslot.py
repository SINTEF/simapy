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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("reference","sima/condition/ModelReferenceVariable","Model reference to be replaced",False))
        self.attributes.append(Attribute("replaceChildren","boolean","If checked the children of the reference will replaced",default=False))
# 
# Generated with RequirementOutputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .outputslot import OutputSlotBlueprint

class RequirementOutputSlotBlueprint(OutputSlotBlueprint):
    """"""

    def __init__(self, name="RequirementOutputSlot", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("useQuery","boolean","Use boolean expressions using operators =, !=,&&,|| to create more advanced queries",default=False))
        self.attributes.append(Attribute("query","string","",default=""))
        self.attributes.append(BlueprintAttribute("userRequirements","sima/post/Requirement","",True,Dimension("size","")))
        self.attributes.append(Attribute("flatten","boolean","",default=False))
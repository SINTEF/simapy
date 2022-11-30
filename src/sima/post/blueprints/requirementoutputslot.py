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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("useQuery","boolean","Use boolean expressions using operators =, !=,&&,|| to create more advanced queries",default=False))
        self.add_attribute(Attribute("query","string",""))
        self.add_attribute(BlueprintAttribute("userRequirements","sima/post/Requirement","",True,Dimension("*")))
        self.add_attribute(Attribute("flatten","boolean","",default=False))
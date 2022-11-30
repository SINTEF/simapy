# 
# Generated with SlotConnectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SlotConnectionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SlotConnection", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("useQuery","boolean","Use boolean expressions using operators =, !=,&&,|| to create more advanced queries",default=False))
        self.add_attribute(Attribute("query","string",""))
        self.add_attribute(BlueprintAttribute("userRequirements","sima/post/Requirement","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("points","sima/graph/Point","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("toSlot","sima/post/InputSlot","",False))
        self.add_attribute(BlueprintAttribute("fromSlot","sima/post/OutputSlot","",False))
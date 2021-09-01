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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("useQuery","boolean","Use boolean expressions using operators =, !=,&&,|| to create more advanced queries",default=False))
        self.attributes.append(Attribute("query","string","",default=""))
        self.attributes.append(BlueprintAttribute("userRequirements","sima/post/Requirement","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("points","sima/graph/Point","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("toSlot","sima/post/InputSlot","",False))
        self.attributes.append(BlueprintAttribute("fromSlot","sima/post/OutputSlot","",False))
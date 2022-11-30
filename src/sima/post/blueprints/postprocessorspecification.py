# 
# Generated with PostProcessorSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class PostProcessorSpecificationBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="PostProcessorSpecification", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("nodes","sima/post/OperationNode","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("connections","sima/post/SlotConnection","",True,Dimension("*")))
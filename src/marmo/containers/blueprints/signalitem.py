# 
# Generated with SignalItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class SignalItemBlueprint(NamedEntityBlueprint):
    """"""

    def __init__(self, name="SignalItem", package_path="marmo/containers", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
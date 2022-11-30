# Signal base type
# Generated with SignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signalitem import SignalItemBlueprint

class SignalBlueprint(SignalItemBlueprint):
    """Signal base type"""

    def __init__(self, name="Signal", package_path="marmo/containers", description="Signal base type"):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
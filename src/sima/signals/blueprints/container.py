# Containers contain signals and other containers
# Generated with ContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signalitem import SignalItemBlueprint

class ContainerBlueprint(SignalItemBlueprint):
    """Containers contain signals and other containers"""

    def __init__(self, name="Container", package_path="sima/signals", description="Containers contain signals and other containers"):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","",optional=False))
        self.add_attribute(BlueprintAttribute("attributes","sima/signals/Attribute","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("signals","sima/signals/Signal","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("containers","sima/signals/Container","",True,Dimension("*")))
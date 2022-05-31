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

    def __init__(self, name="Container", package_path="marmo/containers", description="Containers contain signals and other containers"):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("signals","marmo/containers/Signal","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("containers","marmo/containers/Container","",True,Dimension("*")))
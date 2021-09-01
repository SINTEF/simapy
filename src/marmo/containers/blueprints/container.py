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
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("attributes","/containers/Attribute","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("signals","/containers/Signal","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("containers","/containers/Container","",True,Dimension("size","")))
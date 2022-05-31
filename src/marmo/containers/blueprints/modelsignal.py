# 
# Generated with ModelSignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signal import SignalBlueprint

class ModelSignalBlueprint(SignalBlueprint):
    """"""

    def __init__(self, name="ModelSignal", package_path="marmo/containers", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("value","marmosystem/SIMOS/NamedEntity","",True))
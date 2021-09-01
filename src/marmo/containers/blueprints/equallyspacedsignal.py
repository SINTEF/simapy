# Data model for an equally spaced signal.
# Generated with EquallySpacedSignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signal import SignalBlueprint

class EquallySpacedSignalBlueprint(SignalBlueprint):
    """Data model for an equally spaced signal."""

    def __init__(self, name="EquallySpacedSignal", package_path="marmo/containers", description="Data model for an equally spaced signal."):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("attributes","/containers/Attribute","",True,Dimension("size","")))
        self.attributes.append(Attribute("value","number","",Dimension("size","")))
        self.attributes.append(Attribute("xstart","number",""))
        self.attributes.append(Attribute("xdelta","number",""))
        self.attributes.append(Attribute("unit","string",""))
        self.attributes.append(Attribute("xunit","string",""))
        self.attributes.append(Attribute("xname","string",""))
        self.attributes.append(Attribute("xlabel","string",""))
        self.attributes.append(Attribute("xdescription","string",""))
        self.attributes.append(Attribute("label","string",""))
        self.attributes.append(Attribute("legend","string",""))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.attributes.append(Attribute("value","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("xstart","number","",default=0.0))
        self.attributes.append(Attribute("xdelta","number","",default=1.0))
        self.attributes.append(Attribute("unit","string","",default=""))
        self.attributes.append(Attribute("xunit","string","",default=""))
        self.attributes.append(Attribute("xname","string","",default=""))
        self.attributes.append(Attribute("xlabel","string","",default=""))
        self.attributes.append(Attribute("xdescription","string","",default=""))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("legend","string","",default=""))
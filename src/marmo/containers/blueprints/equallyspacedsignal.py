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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.add_attribute(Attribute("value","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("xstart","number","",default=0.0))
        self.add_attribute(Attribute("xdelta","number","",default=1.0))
        self.add_attribute(Attribute("unit","string",""))
        self.add_attribute(Attribute("xunit","string",""))
        self.add_attribute(Attribute("xname","string",""))
        self.add_attribute(Attribute("xlabel","string",""))
        self.add_attribute(Attribute("xdescription","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("legend","string",""))
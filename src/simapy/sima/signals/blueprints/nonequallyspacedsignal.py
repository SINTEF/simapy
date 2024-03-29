# Data model for a non-equally spaced signal.
# Generated with NonEquallySpacedSignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signal import SignalBlueprint

class NonEquallySpacedSignalBlueprint(SignalBlueprint):
    """Data model for a non-equally spaced signal."""

    def __init__(self, name="NonEquallySpacedSignal", package_path="sima/signals", description="Data model for a non-equally spaced signal."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","",optional=False))
        self.add_attribute(BlueprintAttribute("attributes","sima/signals/Attribute","",True,Dimension("*")))
        self.add_attribute(Attribute("xvalue","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("value","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("unit","string",""))
        self.add_attribute(Attribute("xunit","string",""))
        self.add_attribute(Attribute("xname","string",""))
        self.add_attribute(Attribute("xlabel","string",""))
        self.add_attribute(Attribute("xdescription","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("legend","string",""))
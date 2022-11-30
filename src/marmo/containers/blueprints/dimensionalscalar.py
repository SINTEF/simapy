# Single scalar value with dimension
# Generated with DimensionalScalarBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signal import SignalBlueprint

class DimensionalScalarBlueprint(SignalBlueprint):
    """Single scalar value with dimension"""

    def __init__(self, name="DimensionalScalar", package_path="marmo/containers", description="Single scalar value with dimension"):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.add_attribute(Attribute("value","number","",default=0.0))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("unit","string",""))
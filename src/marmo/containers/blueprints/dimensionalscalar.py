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
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("attributes","/containers/Attribute","",True,Dimension("size","")))
        self.attributes.append(Attribute("value","number",""))
        self.attributes.append(Attribute("label","string",""))
        self.attributes.append(Attribute("unit","string",""))
# 2D matrix of values with dimension
# Generated with DimensionalMatrixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signal import SignalBlueprint

class DimensionalMatrixBlueprint(SignalBlueprint):
    """2D matrix of values with dimension"""

    def __init__(self, name="DimensionalMatrix", package_path="marmo/containers", description="2D matrix of values with dimension"):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.add_attribute(Attribute("value","number","",Dimension("*"),Dimension("*"),default=0.0))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("unit","string","",Dimension("*"),Dimension("*")))
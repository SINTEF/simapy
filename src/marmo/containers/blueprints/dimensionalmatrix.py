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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(BlueprintAttribute("attributes","marmo/containers/Attribute","",True,Dimension("*")))
        self.attributes.append(Attribute("value","number","",Dimension("*"),Dimension("*"),default=0.0))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("unit","string","",Dimension("*"),Dimension("*"),default=""))
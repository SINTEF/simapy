# CONTOUR LINES OF HS-TP.
# Generated with ContourBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class ContourBlueprint(EntityBlueprint):
    """CONTOUR LINES OF HS-TP."""

    def __init__(self, name="Contour", package_path="metocean/longTermStatistics/wave", description="CONTOUR LINES OF HS-TP."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("Hs","number","Hs.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("Tp","number","Tp",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("returnPeriod","number","return period",default=0.0))
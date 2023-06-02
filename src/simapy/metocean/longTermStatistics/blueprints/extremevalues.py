# EXTREME VALUES FOR DIFFERENT PROBABILITY.
# Generated with ExtremeValuesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class ExtremeValuesBlueprint(EntityBlueprint):
    """EXTREME VALUES FOR DIFFERENT PROBABILITY."""

    def __init__(self, name="ExtremeValues", package_path="metocean/longTermStatistics", description="EXTREME VALUES FOR DIFFERENT PROBABILITY."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("variable","string","variable."))
        self.add_attribute(Attribute("returnPeriods","number","return periods",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("extremes","number","extreme values for the variable",Dimension("*"),default=0.0))
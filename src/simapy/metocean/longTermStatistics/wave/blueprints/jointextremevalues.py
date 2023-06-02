# JOINED EXTREME VALUES FOR DIFFERENT PROBABILITY.
# Generated with JointExtremeValuesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class JointExtremeValuesBlueprint(EntityBlueprint):
    """JOINED EXTREME VALUES FOR DIFFERENT PROBABILITY."""

    def __init__(self, name="JointExtremeValues", package_path="metocean/longTermStatistics/wave", description="JOINED EXTREME VALUES FOR DIFFERENT PROBABILITY."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("var1","string","first variable."))
        self.add_attribute(Attribute("var2","string","second variable."))
        self.add_attribute(Attribute("returnPeriods","number","return periods",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("var1Extremes","number","extreme values for the variable 1",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("var2Extremes","number","extreme values for the variable 2",Dimension("*"),default=0.0))
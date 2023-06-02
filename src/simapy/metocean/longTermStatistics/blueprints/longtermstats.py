# Description for long term statistical metocean data.
# Generated with LongTermStatsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class LongTermStatsBlueprint(NamedEntityBlueprint):
    """Description for long term statistical metocean data."""

    def __init__(self, name="LongTermStats", package_path="metocean/longTermStatistics", description="Description for long term statistical metocean data."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the metocean data."))
        self.add_attribute(BlueprintAttribute("periods","metocean/longTermStatistics/Period","statistical model for different time periods.",True,Dimension("*")))
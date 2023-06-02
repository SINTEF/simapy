# Description for stochastic process with sampling at certain period.
# Generated with PeriodBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class PeriodBlueprint(NamedEntityBlueprint):
    """Description for stochastic process with sampling at certain period."""

    def __init__(self, name="Period", package_path="metocean/longTermStatistics", description="Description for stochastic process with sampling at certain period."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name of the time period as seen in SIMA."))
        self.add_attribute(Attribute("period","string","place holder identification for the time period e.g. Year, Jan"))
        self.add_attribute(BlueprintAttribute("wave","metocean/longTermStatistics/wave/Stat","models for statistical representation of wave, e.g. omni, or 12sec.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("wind","metocean/longTermStatistics/level/Stat","models for statistical representation of wind, e.g. omni, or 12sec.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("current","metocean/longTermStatistics/level/Stat","models for statistical representation of current, e.g. omni, or 12sec.",True,Dimension("*")))
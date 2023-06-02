# Description for stochastic process with sampling.
# Generated with StatBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class StatBlueprint(NamedEntityBlueprint):
    """Description for stochastic process with sampling."""

    def __init__(self, name="Stat", package_path="metocean/longTermStatistics/level", description="Description for stochastic process with sampling."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for this statistical data, wind/current, which appear in SIMA, e.g. wind_12sec, or current_omni."))
        self.add_attribute(Attribute("duration","number","event duration in hours.",default=0.0))
        self.add_attribute(BlueprintAttribute("levels","metocean/longTermStatistics/level/Profile","statistical representation of wind/current at this level and sampling rate.",True,Dimension("*")))
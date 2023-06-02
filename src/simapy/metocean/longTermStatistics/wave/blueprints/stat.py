# Description for stochastic wave.
# Generated with StatBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class StatBlueprint(NamedEntityBlueprint):
    """Description for stochastic wave."""

    def __init__(self, name="Stat", package_path="metocean/longTermStatistics/wave", description="Description for stochastic wave."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for this statistical data which appear in SIMA, e.g. wave12sec, or waveomni."))
        self.add_attribute(Attribute("duration","number","sampling rate in hours.",default=0.0))
        self.add_attribute(BlueprintAttribute("sectors","metocean/longTermStatistics/wave/Sector","sectoral wave at this sampling rate for Hs.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("omni","metocean/longTermStatistics/wave/Sector","omni wave at this sampling rate for Hs.",True))
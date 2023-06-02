# Description for stochastic process with sampling.
# Generated with ProfileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class ProfileBlueprint(NamedEntityBlueprint):
    """Description for stochastic process with sampling."""

    def __init__(self, name="Profile", package_path="metocean/longTermStatistics/level", description="Description for stochastic process with sampling."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for statistics at this level, e.g. level10m."))
        self.add_attribute(Attribute("level","number","sampling rate in hours.",default=0.0))
        self.add_attribute(BlueprintAttribute("sectors","metocean/longTermStatistics/Sector","sectoral representation of wind/current at this sampling rate.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("omni","metocean/longTermStatistics/Sector","omni representation of wind/current at this sampling rate.",True))
        self.add_attribute(BlueprintAttribute("sectoralHsBinned","metocean/longTermStatistics/HsBinnedSector","sectoral representation of wind/current binned for different Hs at this sampling rate.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("omniHsBinned","metocean/longTermStatistics/HsBinnedSector","omni representation of wind/current binned for different Hs at this sampling rate.",True))
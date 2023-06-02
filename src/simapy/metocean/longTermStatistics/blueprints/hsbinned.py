# Statistical representation of a a sector.
# Generated with HsBinnedBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class HsBinnedBlueprint(NamedEntityBlueprint):
    """Statistical representation of a a sector."""

    def __init__(self, name="HsBinned", package_path="metocean/longTermStatistics", description="Statistical representation of a a sector."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","unique name for this bin."))
        self.add_attribute(Attribute("upperHsLimit","number","mean sector direction.",default=0.0))
        self.add_attribute(Attribute("lowerHsLimit","number","mean sector direction.",default=0.0))
        self.add_attribute(BlueprintAttribute("weibullDistribution","metocean/longTermStatistics/Weibull","Weibull parameters.",True))
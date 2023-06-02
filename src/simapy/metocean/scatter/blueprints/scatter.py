# Description for scatter data based on Hs-Tp.
# Generated with ScatterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class ScatterBlueprint(NamedEntityBlueprint):
    """Description for scatter data based on Hs-Tp."""

    def __init__(self, name="Scatter", package_path="metocean/scatter", description="Description for scatter data based on Hs-Tp."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the scatter data as appear in SIMA."))
        self.add_attribute(Attribute("hsUpperLimits","number","upper limits of the boundaries for each row in the scatter data.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("tpUpperLimits","number","upper limits of the boundaries for each column in the scatter data.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("seaStateDuration","number","duration of sea state.",default=0.0))
        self.add_attribute(Attribute("countingPeriod","number","the duration which is used to count the occurrence of events.",default=0.0))
        self.add_attribute(BlueprintAttribute("sectors","metocean/scatter/Sector","sector scatter data.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("omni","metocean/scatter/Sector","omni scatter data.",True))
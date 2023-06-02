# Description for scatter data based on Hs-Tp.
# Generated with MetoceanBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class MetoceanBlueprint(NamedEntityBlueprint):
    """Description for scatter data based on Hs-Tp."""

    def __init__(self, name="Metocean", package_path="metocean", description="Description for scatter data based on Hs-Tp."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the metocean data."))
        self.add_attribute(BlueprintAttribute("hindcasts","metocean/hindcast/Hindcast","hindcast data.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("scatters","metocean/scatter/Scatter","scatter data.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("longterms","metocean/longTermStatistics/LongTermStats","scatter data.",True,Dimension("*")))
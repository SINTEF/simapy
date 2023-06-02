# Description for hindcast metocean data.
# Generated with HindcastBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class HindcastBlueprint(NamedEntityBlueprint):
    """Description for hindcast metocean data."""

    def __init__(self, name="Hindcast", package_path="metocean/hindcast", description="Description for hindcast metocean data."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the metocean data."))
        self.add_attribute(Attribute("date","string","date string.",Dimension("*")))
        self.add_attribute(BlueprintAttribute("wave","metocean/hindcast/StochasticWave","wave models.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("wind","metocean/hindcast/StochasticWind","wind models.",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("current","metocean/hindcast/StochasticCurrent","current models.",True,Dimension("*")))
        self.add_attribute(Attribute("latitude","number","",default=0.0))
        self.add_attribute(Attribute("longitude","number","",default=0.0))
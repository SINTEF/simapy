# Description for stochastic wind.
# Generated with StochasticWindBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class StochasticWindBlueprint(NamedEntityBlueprint):
    """Description for stochastic wind."""

    def __init__(self, name="StochasticWind", package_path="metocean/hindcast", description="Description for stochastic wind."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the metocean data.",optional=False))
        self.add_attribute(Attribute("speed","number","mean wind speed.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("direction","number","wind direction.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("level","number","at this level, upward positive.",optional=False,default=0.0))
# Description for stochastic wave.
# Generated with StochasticWaveBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class StochasticWaveBlueprint(NamedEntityBlueprint):
    """Description for stochastic wave."""

    def __init__(self, name="StochasticWave", package_path="metocean/hindcast", description="Description for stochastic wave."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the metocean data.",optional=False))
        self.add_attribute(Attribute("hs","number","significant wave height.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("tp","number","peack period.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("tm","number","mean period.",default=0.0))
        self.add_attribute(Attribute("direction","number","dominant wave direction.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("meanDirection","number","mean wave direction.",default=0.0))
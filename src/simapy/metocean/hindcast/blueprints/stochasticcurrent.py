# Description for stochastic current.
# Generated with StochasticCurrentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class StochasticCurrentBlueprint(NamedEntityBlueprint):
    """Description for stochastic current."""

    def __init__(self, name="StochasticCurrent", package_path="metocean/hindcast", description="Description for stochastic current."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","name for the metocean data."))
        self.add_attribute(Attribute("speed","number","mean current speed.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("direction","number","current direction.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("level","number","at this level, upward positive.",optional=False,default=0.0))
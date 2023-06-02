# Description for stochastic process at a sector.
# Generated with WaveBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class WaveBlueprint(EntityBlueprint):
    """Description for stochastic process at a sector."""

    def __init__(self, name="Wave", package_path="metocean/scatter", description="Description for stochastic process at a sector."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("occurrence","integer","the scatter data for occurrence of Hs-Tp.",Dimension("*"),Dimension("*"),default=0))
# Description for stochastic process at a sector.
# Generated with SectorsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class SectorsBlueprint(EntityBlueprint):
    """Description for stochastic process at a sector."""

    def __init__(self, name="Sectors", package_path="metocean/longTermStatistics/level", description="Description for stochastic process at a sector."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("direction","number","sector direction.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("sectorSize","number","sector size.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("probability","number","probability of this combination",Dimension("*"),default=0.0))
# Description weibull statistics.
# Generated with WeibullBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class WeibullBlueprint(EntityBlueprint):
    """Description weibull statistics."""

    def __init__(self, name="Weibull", package_path="metocean/longTermStatistics/wave", description="Description weibull statistics."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("variable","string","variable."))
        self.add_attribute(Attribute("shape","number","shape.",default=0.0))
        self.add_attribute(Attribute("scale","number","scale.",default=0.0))
        self.add_attribute(Attribute("location","number","location.",default=0.0))
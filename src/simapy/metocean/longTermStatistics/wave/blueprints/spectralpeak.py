# Spectral peak for Tp as a function of Hs.
# Generated with SpectralPeakBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class SpectralPeakBlueprint(EntityBlueprint):
    """Spectral peak for Tp as a function of Hs."""

    def __init__(self, name="SpectralPeak", package_path="metocean/longTermStatistics/wave", description="Spectral peak for Tp as a function of Hs."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("Hs","number","Hs.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("int5","number","5%-interval",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("mean","number","mean.",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("int95","number","95 %-interval",Dimension("*"),default=0.0))
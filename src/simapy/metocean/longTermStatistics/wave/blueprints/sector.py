# Description for wave at a sector.
# Generated with SectorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.namedentity import NamedEntityBlueprint

class SectorBlueprint(NamedEntityBlueprint):
    """Description for wave at a sector."""

    def __init__(self, name="Sector", package_path="metocean/longTermStatistics/wave", description="Description for wave at a sector."):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","unique name for the sector, e.g. sec120, or omni."))
        self.add_attribute(Attribute("direction","number","mean sector direction.",default=0.0))
        self.add_attribute(Attribute("sectorSize","number","sector size.",default=0.0))
        self.add_attribute(Attribute("probability","number","probability of this combination",default=0.0))
        self.add_attribute(BlueprintAttribute("weibullDistribution","metocean/longTermStatistics/wave/Weibull","weibull parameters for Hs.",True))
        self.add_attribute(BlueprintAttribute("extremeValues","metocean/longTermStatistics/wave/JointExtremeValues","joined extreme values for Hs and Tp.",True))
        self.add_attribute(BlueprintAttribute("spectralPeak","metocean/longTermStatistics/wave/SpectralPeak","Spectral peak period as a function of Hs.",True))
        self.add_attribute(BlueprintAttribute("contours","metocean/longTermStatistics/wave/Contour","Hs-Tp contours",True,Dimension("*")))
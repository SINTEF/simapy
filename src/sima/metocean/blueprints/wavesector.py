# 
# Generated with WaveSectorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WaveSectorBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WaveSector", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("contours","sima/metocean/ContourData","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("spectralPeakRelation","sima/metocean/SpectralPeakPeriodRelation","",True))
        self.add_attribute(BlueprintAttribute("significantWaveHeightWeibullData","sima/metocean/SignificantWaveHeightWeibullData","",True))
        self.add_attribute(Attribute("direction","number","",default=0.0))
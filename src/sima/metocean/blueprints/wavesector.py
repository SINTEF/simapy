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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("contours","sima/metocean/ContourData","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("spectralPeakRelation","sima/metocean/SpectralPeakPeriodRelation","",True))
        self.attributes.append(BlueprintAttribute("significantWaveHeightWeibullData","sima/metocean/SignificantWaveHeightWeibullData","",True))
        self.attributes.append(Attribute("direction","number","",default=0.0))
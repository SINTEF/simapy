# 
# Generated with DisturbedWaveFieldBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class DisturbedWaveFieldBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DisturbedWaveField", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("waveFieldFile","string","HDF5 file with wave field definition"))
        self.add_attribute(BlueprintAttribute("diffractorBody","sima/simo/SIMOBody","",False))
        self.add_attribute(Attribute("numHeadings","integer","Number of wave headings the shielding field is interpolated over",default=36))
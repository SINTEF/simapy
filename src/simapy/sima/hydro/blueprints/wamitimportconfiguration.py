# 
# Generated with WamitImportConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class WamitImportConfigurationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WamitImportConfiguration", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("retardationFunctionParameters","sima/hydro/RetardationFunctionCalculationParameters","",True))
        self.add_attribute(EnumAttribute("waveDriftForce","sima/hydro/WamitWaveDriftForceOption",""))
        self.add_attribute(EnumAttribute("waveForce","sima/hydro/WamitWaveForceOption",""))
        self.add_attribute(EnumAttribute("sumQTF","sima/hydro/WamitQtfImportOption",""))
        self.add_attribute(EnumAttribute("diffQTF","sima/hydro/WamitQtfImportOption",""))
        self.add_attribute(Attribute("diffractedWaveElevation","boolean","",default=True))
        self.add_attribute(Attribute("diffractedWaveVelocity","boolean","",default=True))
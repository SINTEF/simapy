# 
# Generated with SIFImportConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class SIFImportConfigurationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIFImportConfiguration", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("taskName","string","Name of task to import into. Required if bodyName is set."))
        self.add_attribute(Attribute("bodyName","string","Optional. Name of SIMOBody to merge hydrodynamic data into."))
        self.add_attribute(EnumAttribute("waveDriftOption","sima/hydro/SecondOrderWaveDriftOption",""))
        self.add_attribute(EnumAttribute("qtfImportOption","sima/hydro/QTFImportOption",""))
        self.add_attribute(Attribute("overrideConstants","boolean","Override the water depth and physical constants of the task being imported into with the values from the file. Off keeps the values the task already has, and is what a run with no answer uses.",default=False))
        self.add_attribute(BlueprintAttribute("retardationFunctionParameters","sima/hydro/RetardationFunctionCalculationParameters","",True))
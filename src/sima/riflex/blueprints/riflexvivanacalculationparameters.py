# 
# Generated with RIFLEXVivanaCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RIFLEXVivanaCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RIFLEXVivanaCalculationParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("eigenvalueAnalysisParameters","sima/riflex/EigenvalueAnalysisParameters","",True))
        self.add_attribute(BlueprintAttribute("responseAnalysisParameters","sima/riflex/ResponseAnalysisParameters","",True))
        self.add_attribute(BlueprintAttribute("fatigueProperties","sima/riflex/FatigueProperties","",True))
        self.add_attribute(EnumAttribute("vivLoadType","sima/riflex/VIVLoadType","Option for type of VIV loads to be applied"))
        self.add_attribute(Attribute("waterTemperature","number","Water temperature",default=4.0))
        self.add_attribute(EnumAttribute("randomGenerator","sima/simo/RandomGenerator",""))
        self.add_attribute(BlueprintAttribute("hydrodynamicCrossSectionProperties","sima/riflex/HydrodynamicCrossSectionProperties","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("excitationZoneProperties","sima/riflex/ExcitationZoneProperty","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("addedMassProperties","sima/riflex/AddedMassProperty","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("excitationCoefficientProperties","sima/riflex/ExcitationCoefficientsProperty","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("dampingFactorProperties","sima/riflex/DampingFactorProperty","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("strouhalSpecificationProperties","sima/riflex/StrouhalSpecificationProperty","",True,Dimension("*")))
        self.add_attribute(Attribute("addedMassFirstModeNumber","integer","First mode number in the active VIV direction for which the constant still-water added mass will be used.",default=1000000))
        self.add_attribute(Attribute("addedMassLastModeNumber","integer","Last mode number in the active VIV direction for which the full frequency-dependent added mass curves will be used.",default=1000000))
        self.add_attribute(EnumAttribute("addedMassFrequencyDependence","sima/riflex/AddedMassFrequencyDependency",""))
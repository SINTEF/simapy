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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("eigenvalueAnalysisParameters","sima/riflex/EigenvalueAnalysisParameters","",True))
        self.attributes.append(BlueprintAttribute("responseAnalysisParameters","sima/riflex/ResponseAnalysisParameters","",True))
        self.attributes.append(BlueprintAttribute("fatigueProperties","sima/riflex/FatigueProperties","",True))
        self.attributes.append(EnumAttribute("vivLoadType","sima/riflex/VIVLoadType","Option for type of VIV loads to be applied"))
        self.attributes.append(Attribute("waterTemperature","number","Water temperature",default=4.0))
        self.attributes.append(EnumAttribute("randomGenerator","sima/simo/RandomGenerator",""))
        self.attributes.append(BlueprintAttribute("hydrodynamicCrossSectionProperties","sima/riflex/HydrodynamicCrossSectionProperties","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("excitationZoneProperties","sima/riflex/ExcitationZoneProperty","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("addedMassProperties","sima/riflex/AddedMassProperty","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("excitationCoefficientProperties","sima/riflex/ExcitationCoefficientsProperty","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("dampingFactorProperties","sima/riflex/DampingFactorProperty","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("strouhalSpecificationProperties","sima/riflex/StrouhalSpecificationProperty","",True,Dimension("size","")))
        self.attributes.append(Attribute("addedMassFirstModeNumber","integer","First mode number in the active VIV direction for which the constant still-water added mass will be used.",default=1000000))
        self.attributes.append(Attribute("addedMassLastModeNumber","integer","Last mode number in the active VIV direction for which the full frequency-dependent added mass curves will be used.",default=1000000))
        self.attributes.append(EnumAttribute("addedMassFrequencyDependence","sima/riflex/AddedMassFrequencyDependency",""))
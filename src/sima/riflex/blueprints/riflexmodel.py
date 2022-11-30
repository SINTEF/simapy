# 
# Generated with RIFLEXModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.simo.blueprints.simomodel import SIMOModelBlueprint

class RIFLEXModelBlueprint(SIMOModelBlueprint):
    """"""

    def __init__(self, name="RIFLEXModel", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("environments","sima/environment/Environment","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("airfoils","sima/windturbine/Airfoil","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("location","sima/riflex/RIFLEXLocation","",True))
        self.add_attribute(BlueprintAttribute("bodies","sima/simo/SIMOBody","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hydrodynamicCouplings","sima/simo/HydrodynamicCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("simpleWireCouplings","sima/simo/SimpleWireCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("fixedElongationCouplings","sima/simo/FixedElongationCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("dockingCones","sima/simo/DockingCone","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("pointFenders","sima/simo/PointFender","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("rollerFenders","sima/simo/RollerFender","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("ratchets","sima/simo/RatchetCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("multipleWireCouplings","sima/simo/MultipleWireCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("bumperGroups","sima/simo/BumperGroup","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("advancedBumpers","sima/simo/AdvancedBumper","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("liftLineCouplings","sima/simo/LiftLineCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("momentCouplings","sima/simo/MomentCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("sIMOStaticCalculationParameters","sima/simo/SIMOStaticCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("sIMODynamicCalculationParameters","sima/simo/SIMODynamicCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("stabilityCalculationParameters","sima/simo/StabilityCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("simoFrequencyDomainCalculation","sima/simo/SIMOFrequencyDomainCalculation","",True))
        self.add_attribute(BlueprintAttribute("fibreRopeModels","sima/simo/FibreRopeModel","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("slenderSystem","sima/riflex/SlenderSystem","",True))
        self.add_attribute(BlueprintAttribute("supportVessels","sima/riflex/SupportVessel","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("referenceFrames","sima/riflex/ReferenceFrame","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("combinedLoadingAnalyses","sima/riflex/CombinedLoading","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("riflexStaticCalculationParameters","sima/riflex/RIFLEXStaticCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("riflexDynamicCalculationParameters","sima/riflex/RIFLEXDynamicCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("riflexEigenvalueCalculationParameters","sima/riflex/RIFLEXEigenvalueCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("riflexVivanaCalculationParameters","sima/riflex/RIFLEXVivanaCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("potentialFlowLibrary","sima/riflex/PotentialFlowLibrary","",True))
        self.add_attribute(BlueprintAttribute("fatigueAnalyses","sima/riflex/FatigueAnalysis","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("snCurves","sima/riflex/SNCurve","",True,Dimension("*")))
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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("environments","sima/environment/Environment","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("airfoils","sima/windturbine/Airfoil","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("location","sima/simo/CommonLocation","",True))
        self.attributes.append(BlueprintAttribute("bodies","sima/simo/SIMOBody","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("hydrodynamicCouplings","sima/simo/HydrodynamicCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("simpleWireCouplings","sima/simo/SimpleWireCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("fixedElongationCouplings","sima/simo/FixedElongationCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("dockingCones","sima/simo/DockingCone","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("pointFenders","sima/simo/PointFender","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("rollerFenders","sima/simo/RollerFender","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("ratchets","sima/simo/RatchetCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("multipleWireCouplings","sima/simo/MultipleWireCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("bumperGroups","sima/simo/BumperGroup","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("advancedBumpers","sima/simo/AdvancedBumper","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("liftLineCouplings","sima/simo/LiftLineCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("momentCouplings","sima/simo/MomentCoupling","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("sIMOStaticCalculationParameters","sima/simo/SIMOStaticCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("sIMODynamicCalculationParameters","sima/simo/SIMODynamicCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("stabilityCalculationParameters","sima/simo/StabilityCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("simoFrequencyDomainCalculation","sima/simo/SIMOFrequencyDomainCalculation","",True))
        self.attributes.append(BlueprintAttribute("fibreRopeModels","sima/simo/FibreRopeModel","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("slenderSystem","sima/riflex/SlenderSystem","",True))
        self.attributes.append(BlueprintAttribute("supportVessels","sima/riflex/SupportVessel","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("referenceFrames","sima/riflex/ReferenceFrame","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("combinedLoadingAnalyses","sima/riflex/CombinedLoading","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("riflexStaticCalculationParameters","sima/riflex/RIFLEXStaticCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("riflexDynamicCalculationParameters","sima/riflex/RIFLEXDynamicCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("riflexEigenvalueCalculationParameters","sima/riflex/RIFLEXEigenvalueCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("riflexVivanaCalculationParameters","sima/riflex/RIFLEXVivanaCalculationParameters","",True))
        self.attributes.append(BlueprintAttribute("potentialFlowLibrary","sima/riflex/PotentialFlowLibrary","",True))
        self.attributes.append(BlueprintAttribute("fatigueAnalyses","sima/riflex/FatigueAnalysis","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("snCurves","sima/riflex/SNCurve","",True,Dimension("size","")))
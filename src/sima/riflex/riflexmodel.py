# This an autogenerated file
# 
# Generated with RIFLEXModel
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexmodel import RIFLEXModelBlueprint
from typing import Dict
from sima.environment.environment import Environment
from sima.riflex.combinedloading import CombinedLoading
from sima.riflex.fatigueanalysis import FatigueAnalysis
from sima.riflex.potentialflowlibrary import PotentialFlowLibrary
from sima.riflex.referenceframe import ReferenceFrame
from sima.riflex.riflexdynamiccalculationparameters import RIFLEXDynamicCalculationParameters
from sima.riflex.riflexeigenvaluecalculationparameters import RIFLEXEigenvalueCalculationParameters
from sima.riflex.riflexlocation import RIFLEXLocation
from sima.riflex.riflexstaticcalculationparameters import RIFLEXStaticCalculationParameters
from sima.riflex.riflexvivanacalculationparameters import RIFLEXVivanaCalculationParameters
from sima.riflex.slendersystem import SlenderSystem
from sima.riflex.sncurve import SNCurve
from sima.riflex.supportvessel import SupportVessel
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.advancedbumper import AdvancedBumper
from sima.simo.bumpergroup import BumperGroup
from sima.simo.dockingcone import DockingCone
from sima.simo.fibreropemodel import FibreRopeModel
from sima.simo.fixedelongationcoupling import FixedElongationCoupling
from sima.simo.hydrodynamiccoupling import HydrodynamicCoupling
from sima.simo.liftlinecoupling import LiftLineCoupling
from sima.simo.momentcoupling import MomentCoupling
from sima.simo.multiplewirecoupling import MultipleWireCoupling
from sima.simo.pointfender import PointFender
from sima.simo.ratchetcoupling import RatchetCoupling
from sima.simo.rollerfender import RollerFender
from sima.simo.simobody import SIMOBody
from sima.simo.simodynamiccalculationparameters import SIMODynamicCalculationParameters
from sima.simo.simofrequencydomaincalculation import SIMOFrequencyDomainCalculation
from sima.simo.simomodel import SIMOModel
from sima.simo.simostaticcalculationparameters import SIMOStaticCalculationParameters
from sima.simo.simplewirecoupling import SimpleWireCoupling
from sima.simo.stabilitycalculationparameters import StabilityCalculationParameters
from sima.windturbine.airfoil import Airfoil

class RIFLEXModel(SIMOModel):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    environments : List[Environment]
    airfoils : List[Airfoil]
    location : RIFLEXLocation
    bodies : List[SIMOBody]
    hydrodynamicCouplings : List[HydrodynamicCoupling]
    simpleWireCouplings : List[SimpleWireCoupling]
    fixedElongationCouplings : List[FixedElongationCoupling]
    dockingCones : List[DockingCone]
    pointFenders : List[PointFender]
    rollerFenders : List[RollerFender]
    ratchets : List[RatchetCoupling]
    multipleWireCouplings : List[MultipleWireCoupling]
    bumperGroups : List[BumperGroup]
    advancedBumpers : List[AdvancedBumper]
    liftLineCouplings : List[LiftLineCoupling]
    momentCouplings : List[MomentCoupling]
    sIMOStaticCalculationParameters : SIMOStaticCalculationParameters
    sIMODynamicCalculationParameters : SIMODynamicCalculationParameters
    stabilityCalculationParameters : StabilityCalculationParameters
    simoFrequencyDomainCalculation : SIMOFrequencyDomainCalculation
    fibreRopeModels : List[FibreRopeModel]
    slenderSystem : SlenderSystem
    supportVessels : List[SupportVessel]
    referenceFrames : List[ReferenceFrame]
    combinedLoadingAnalyses : List[CombinedLoading]
    riflexStaticCalculationParameters : RIFLEXStaticCalculationParameters
    riflexDynamicCalculationParameters : RIFLEXDynamicCalculationParameters
    riflexEigenvalueCalculationParameters : RIFLEXEigenvalueCalculationParameters
    riflexVivanaCalculationParameters : RIFLEXVivanaCalculationParameters
    potentialFlowLibrary : PotentialFlowLibrary
    fatigueAnalyses : List[FatigueAnalysis]
    snCurves : List[SNCurve]
    """

    def __init__(self , description="", _id=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.environments = list()
        self.airfoils = list()
        self.location = None
        self.bodies = list()
        self.hydrodynamicCouplings = list()
        self.simpleWireCouplings = list()
        self.fixedElongationCouplings = list()
        self.dockingCones = list()
        self.pointFenders = list()
        self.rollerFenders = list()
        self.ratchets = list()
        self.multipleWireCouplings = list()
        self.bumperGroups = list()
        self.advancedBumpers = list()
        self.liftLineCouplings = list()
        self.momentCouplings = list()
        self.sIMOStaticCalculationParameters = None
        self.sIMODynamicCalculationParameters = None
        self.stabilityCalculationParameters = None
        self.simoFrequencyDomainCalculation = None
        self.fibreRopeModels = list()
        self.slenderSystem = None
        self.supportVessels = list()
        self.referenceFrames = list()
        self.combinedLoadingAnalyses = list()
        self.riflexStaticCalculationParameters = None
        self.riflexDynamicCalculationParameters = None
        self.riflexEigenvalueCalculationParameters = None
        self.riflexVivanaCalculationParameters = None
        self.potentialFlowLibrary = None
        self.fatigueAnalyses = list()
        self.snCurves = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXModelBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def environments(self) -> List[Environment]:
        """"""
        return self.__environments

    @environments.setter
    def environments(self, value: List[Environment]):
        """Set environments"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__environments = value

    @property
    def airfoils(self) -> List[Airfoil]:
        """"""
        return self.__airfoils

    @airfoils.setter
    def airfoils(self, value: List[Airfoil]):
        """Set airfoils"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__airfoils = value

    @property
    def location(self) -> RIFLEXLocation:
        """"""
        return self.__location

    @location.setter
    def location(self, value: RIFLEXLocation):
        """Set location"""
        self.__location = value

    @property
    def bodies(self) -> List[SIMOBody]:
        """"""
        return self.__bodies

    @bodies.setter
    def bodies(self, value: List[SIMOBody]):
        """Set bodies"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__bodies = value

    @property
    def hydrodynamicCouplings(self) -> List[HydrodynamicCoupling]:
        """"""
        return self.__hydrodynamicCouplings

    @hydrodynamicCouplings.setter
    def hydrodynamicCouplings(self, value: List[HydrodynamicCoupling]):
        """Set hydrodynamicCouplings"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__hydrodynamicCouplings = value

    @property
    def simpleWireCouplings(self) -> List[SimpleWireCoupling]:
        """"""
        return self.__simpleWireCouplings

    @simpleWireCouplings.setter
    def simpleWireCouplings(self, value: List[SimpleWireCoupling]):
        """Set simpleWireCouplings"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__simpleWireCouplings = value

    @property
    def fixedElongationCouplings(self) -> List[FixedElongationCoupling]:
        """"""
        return self.__fixedElongationCouplings

    @fixedElongationCouplings.setter
    def fixedElongationCouplings(self, value: List[FixedElongationCoupling]):
        """Set fixedElongationCouplings"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__fixedElongationCouplings = value

    @property
    def dockingCones(self) -> List[DockingCone]:
        """"""
        return self.__dockingCones

    @dockingCones.setter
    def dockingCones(self, value: List[DockingCone]):
        """Set dockingCones"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__dockingCones = value

    @property
    def pointFenders(self) -> List[PointFender]:
        """"""
        return self.__pointFenders

    @pointFenders.setter
    def pointFenders(self, value: List[PointFender]):
        """Set pointFenders"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__pointFenders = value

    @property
    def rollerFenders(self) -> List[RollerFender]:
        """"""
        return self.__rollerFenders

    @rollerFenders.setter
    def rollerFenders(self, value: List[RollerFender]):
        """Set rollerFenders"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__rollerFenders = value

    @property
    def ratchets(self) -> List[RatchetCoupling]:
        """"""
        return self.__ratchets

    @ratchets.setter
    def ratchets(self, value: List[RatchetCoupling]):
        """Set ratchets"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__ratchets = value

    @property
    def multipleWireCouplings(self) -> List[MultipleWireCoupling]:
        """"""
        return self.__multipleWireCouplings

    @multipleWireCouplings.setter
    def multipleWireCouplings(self, value: List[MultipleWireCoupling]):
        """Set multipleWireCouplings"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__multipleWireCouplings = value

    @property
    def bumperGroups(self) -> List[BumperGroup]:
        """"""
        return self.__bumperGroups

    @bumperGroups.setter
    def bumperGroups(self, value: List[BumperGroup]):
        """Set bumperGroups"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__bumperGroups = value

    @property
    def advancedBumpers(self) -> List[AdvancedBumper]:
        """"""
        return self.__advancedBumpers

    @advancedBumpers.setter
    def advancedBumpers(self, value: List[AdvancedBumper]):
        """Set advancedBumpers"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__advancedBumpers = value

    @property
    def liftLineCouplings(self) -> List[LiftLineCoupling]:
        """"""
        return self.__liftLineCouplings

    @liftLineCouplings.setter
    def liftLineCouplings(self, value: List[LiftLineCoupling]):
        """Set liftLineCouplings"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__liftLineCouplings = value

    @property
    def momentCouplings(self) -> List[MomentCoupling]:
        """"""
        return self.__momentCouplings

    @momentCouplings.setter
    def momentCouplings(self, value: List[MomentCoupling]):
        """Set momentCouplings"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__momentCouplings = value

    @property
    def sIMOStaticCalculationParameters(self) -> SIMOStaticCalculationParameters:
        """"""
        return self.__sIMOStaticCalculationParameters

    @sIMOStaticCalculationParameters.setter
    def sIMOStaticCalculationParameters(self, value: SIMOStaticCalculationParameters):
        """Set sIMOStaticCalculationParameters"""
        self.__sIMOStaticCalculationParameters = value

    @property
    def sIMODynamicCalculationParameters(self) -> SIMODynamicCalculationParameters:
        """"""
        return self.__sIMODynamicCalculationParameters

    @sIMODynamicCalculationParameters.setter
    def sIMODynamicCalculationParameters(self, value: SIMODynamicCalculationParameters):
        """Set sIMODynamicCalculationParameters"""
        self.__sIMODynamicCalculationParameters = value

    @property
    def stabilityCalculationParameters(self) -> StabilityCalculationParameters:
        """"""
        return self.__stabilityCalculationParameters

    @stabilityCalculationParameters.setter
    def stabilityCalculationParameters(self, value: StabilityCalculationParameters):
        """Set stabilityCalculationParameters"""
        self.__stabilityCalculationParameters = value

    @property
    def simoFrequencyDomainCalculation(self) -> SIMOFrequencyDomainCalculation:
        """"""
        return self.__simoFrequencyDomainCalculation

    @simoFrequencyDomainCalculation.setter
    def simoFrequencyDomainCalculation(self, value: SIMOFrequencyDomainCalculation):
        """Set simoFrequencyDomainCalculation"""
        self.__simoFrequencyDomainCalculation = value

    @property
    def fibreRopeModels(self) -> List[FibreRopeModel]:
        """"""
        return self.__fibreRopeModels

    @fibreRopeModels.setter
    def fibreRopeModels(self, value: List[FibreRopeModel]):
        """Set fibreRopeModels"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__fibreRopeModels = value

    @property
    def slenderSystem(self) -> SlenderSystem:
        """"""
        return self.__slenderSystem

    @slenderSystem.setter
    def slenderSystem(self, value: SlenderSystem):
        """Set slenderSystem"""
        self.__slenderSystem = value

    @property
    def supportVessels(self) -> List[SupportVessel]:
        """"""
        return self.__supportVessels

    @supportVessels.setter
    def supportVessels(self, value: List[SupportVessel]):
        """Set supportVessels"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__supportVessels = value

    @property
    def referenceFrames(self) -> List[ReferenceFrame]:
        """"""
        return self.__referenceFrames

    @referenceFrames.setter
    def referenceFrames(self, value: List[ReferenceFrame]):
        """Set referenceFrames"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__referenceFrames = value

    @property
    def combinedLoadingAnalyses(self) -> List[CombinedLoading]:
        """"""
        return self.__combinedLoadingAnalyses

    @combinedLoadingAnalyses.setter
    def combinedLoadingAnalyses(self, value: List[CombinedLoading]):
        """Set combinedLoadingAnalyses"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__combinedLoadingAnalyses = value

    @property
    def riflexStaticCalculationParameters(self) -> RIFLEXStaticCalculationParameters:
        """"""
        return self.__riflexStaticCalculationParameters

    @riflexStaticCalculationParameters.setter
    def riflexStaticCalculationParameters(self, value: RIFLEXStaticCalculationParameters):
        """Set riflexStaticCalculationParameters"""
        self.__riflexStaticCalculationParameters = value

    @property
    def riflexDynamicCalculationParameters(self) -> RIFLEXDynamicCalculationParameters:
        """"""
        return self.__riflexDynamicCalculationParameters

    @riflexDynamicCalculationParameters.setter
    def riflexDynamicCalculationParameters(self, value: RIFLEXDynamicCalculationParameters):
        """Set riflexDynamicCalculationParameters"""
        self.__riflexDynamicCalculationParameters = value

    @property
    def riflexEigenvalueCalculationParameters(self) -> RIFLEXEigenvalueCalculationParameters:
        """"""
        return self.__riflexEigenvalueCalculationParameters

    @riflexEigenvalueCalculationParameters.setter
    def riflexEigenvalueCalculationParameters(self, value: RIFLEXEigenvalueCalculationParameters):
        """Set riflexEigenvalueCalculationParameters"""
        self.__riflexEigenvalueCalculationParameters = value

    @property
    def riflexVivanaCalculationParameters(self) -> RIFLEXVivanaCalculationParameters:
        """"""
        return self.__riflexVivanaCalculationParameters

    @riflexVivanaCalculationParameters.setter
    def riflexVivanaCalculationParameters(self, value: RIFLEXVivanaCalculationParameters):
        """Set riflexVivanaCalculationParameters"""
        self.__riflexVivanaCalculationParameters = value

    @property
    def potentialFlowLibrary(self) -> PotentialFlowLibrary:
        """"""
        return self.__potentialFlowLibrary

    @potentialFlowLibrary.setter
    def potentialFlowLibrary(self, value: PotentialFlowLibrary):
        """Set potentialFlowLibrary"""
        self.__potentialFlowLibrary = value

    @property
    def fatigueAnalyses(self) -> List[FatigueAnalysis]:
        """"""
        return self.__fatigueAnalyses

    @fatigueAnalyses.setter
    def fatigueAnalyses(self, value: List[FatigueAnalysis]):
        """Set fatigueAnalyses"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__fatigueAnalyses = value

    @property
    def snCurves(self) -> List[SNCurve]:
        """"""
        return self.__snCurves

    @snCurves.setter
    def snCurves(self, value: List[SNCurve]):
        """Set snCurves"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__snCurves = value

# This an autogenerated file
# 
# Generated with RIFLEXDynamicCalculationParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexdynamiccalculationparameters import RIFLEXDynamicCalculationParametersBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .bladepitchfault import BladePitchFault
from .bodyforcestorage import BodyForceStorage
from .bottomcontactstorage import BottomContactStorage
from .boundarychangegroup import BoundaryChangeGroup
from .curvatureresponsestorage import CurvatureResponseStorage
from .displacementresponsestorage import DisplacementResponseStorage
from .dynamicloads import DynamicLoads
from .dynamicpressurevariationitem import DynamicPressureVariationItem
from .dynamictemperaturevariationitem import DynamicTemperatureVariationItem
from .dynamicwinchvariationitem import DynamicWinchVariationItem
from .dynamicwindchange import DynamicWindChange
from .dynmodvisualisationresponses import DynmodVisualisationResponses
from .envelopecurvespecification import EnvelopeCurveSpecification
from .forceresponsestorage import ForceResponseStorage
from .hlaelementforce import HLAElementForce
from .hydrodynamicloadstorage import HydrodynamicLoadStorage
from .importvesselitem import ImportVesselItem
from .irregularresponseanalysis import IrregularResponseAnalysis
from .irregulartimeseriesparameters import IrregularTimeSeriesParameters
from .regularvesselmotion import RegularVesselMotion
from .regularwaveanalaysis import RegularWaveAnalaysis
from .regularwaveloading import RegularWaveLoading
from .segmentlengthvariationitem import SegmentLengthVariationItem
from .stressstorage import StressStorage
from .sumforceresponsestorage import SumForceResponseStorage
from .supportvesselforcestorage import SupportVesselForceStorage
from .timedomainprocedure import TimeDomainProcedure
from .turbinebladeresponsestorage import TurbineBladeResponseStorage
from .turbineresponsestorage import TurbineResponseStorage
from .windturbineshutdown import WindTurbineShutdown

class RIFLEXDynamicCalculationParameters(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    irregularTimeSeries : IrregularTimeSeriesParameters
    irregularResponseAnalysis : IrregularResponseAnalysis
    timeDomainProcedure : TimeDomainProcedure
    envelopeCurveSpecification : EnvelopeCurveSpecification
    displacementResponseStorage : DisplacementResponseStorage
    forceResponseStorage : ForceResponseStorage
    sumForceResponseStorage : SumForceResponseStorage
    curvatureResponseStorage : CurvatureResponseStorage
    stressStorage : StressStorage
    turbineResponseStorage : TurbineResponseStorage
    turbineBladeResponseStorage : TurbineBladeResponseStorage
    supportVesselForceStorage : SupportVesselForceStorage
    bodyForceStorage : BodyForceStorage
    hydrodynamicLoadStorage : HydrodynamicLoadStorage
    hlaElementForces : List[HLAElementForce]
    hlaImportedBodies : List[ImportVesselItem]
    segmentLengthVariations : List[SegmentLengthVariationItem]
    temperatureVariations : List[DynamicTemperatureVariationItem]
    pressureVariations : List[DynamicPressureVariationItem]
    winchVariations : List[DynamicWinchVariationItem]
    dynamicWindChange : DynamicWindChange
    windTurbineShutdown : WindTurbineShutdown
    bladePitchFault : BladePitchFault
    boundaryChangeGroups : List[BoundaryChangeGroup]
    visualisationResponses : DynmodVisualisationResponses
    regularWaveAnalysis : RegularWaveAnalaysis
    regularWaveLoading : RegularWaveLoading
    regularVesselMotions : List[RegularVesselMotion]
    volumeForcesScaling : float
         Scaling of volume forces.(default 1.0)
    specifiedForcesScaling : float
         Scaling of specified (nodal) forces.(default 1.0)
    currentVelocitiesScaling : float
         Scaling of current velocities.(default 1.0)
    changeStaticLoads : bool
         Change applied static loads at the start of the dynamic analysis(default False)
    dynamicLoads : DynamicLoads
    bottomContactStorage : BottomContactStorage
    """

    def __init__(self , description="", volumeForcesScaling=1.0, specifiedForcesScaling=1.0, currentVelocitiesScaling=1.0, changeStaticLoads=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.irregularTimeSeries = None
        self.irregularResponseAnalysis = None
        self.timeDomainProcedure = None
        self.envelopeCurveSpecification = None
        self.displacementResponseStorage = None
        self.forceResponseStorage = None
        self.sumForceResponseStorage = None
        self.curvatureResponseStorage = None
        self.stressStorage = None
        self.turbineResponseStorage = None
        self.turbineBladeResponseStorage = None
        self.supportVesselForceStorage = None
        self.bodyForceStorage = None
        self.hydrodynamicLoadStorage = None
        self.hlaElementForces = list()
        self.hlaImportedBodies = list()
        self.segmentLengthVariations = list()
        self.temperatureVariations = list()
        self.pressureVariations = list()
        self.winchVariations = list()
        self.dynamicWindChange = None
        self.windTurbineShutdown = None
        self.bladePitchFault = None
        self.boundaryChangeGroups = list()
        self.visualisationResponses = None
        self.regularWaveAnalysis = None
        self.regularWaveLoading = None
        self.regularVesselMotions = list()
        self.volumeForcesScaling = volumeForcesScaling
        self.specifiedForcesScaling = specifiedForcesScaling
        self.currentVelocitiesScaling = currentVelocitiesScaling
        self.changeStaticLoads = changeStaticLoads
        self.dynamicLoads = None
        self.bottomContactStorage = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXDynamicCalculationParametersBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def irregularTimeSeries(self) -> IrregularTimeSeriesParameters:
        """"""
        return self.__irregularTimeSeries

    @irregularTimeSeries.setter
    def irregularTimeSeries(self, value: IrregularTimeSeriesParameters):
        """Set irregularTimeSeries"""
        self.__irregularTimeSeries = value

    @property
    def irregularResponseAnalysis(self) -> IrregularResponseAnalysis:
        """"""
        return self.__irregularResponseAnalysis

    @irregularResponseAnalysis.setter
    def irregularResponseAnalysis(self, value: IrregularResponseAnalysis):
        """Set irregularResponseAnalysis"""
        self.__irregularResponseAnalysis = value

    @property
    def timeDomainProcedure(self) -> TimeDomainProcedure:
        """"""
        return self.__timeDomainProcedure

    @timeDomainProcedure.setter
    def timeDomainProcedure(self, value: TimeDomainProcedure):
        """Set timeDomainProcedure"""
        self.__timeDomainProcedure = value

    @property
    def envelopeCurveSpecification(self) -> EnvelopeCurveSpecification:
        """"""
        return self.__envelopeCurveSpecification

    @envelopeCurveSpecification.setter
    def envelopeCurveSpecification(self, value: EnvelopeCurveSpecification):
        """Set envelopeCurveSpecification"""
        self.__envelopeCurveSpecification = value

    @property
    def displacementResponseStorage(self) -> DisplacementResponseStorage:
        """"""
        return self.__displacementResponseStorage

    @displacementResponseStorage.setter
    def displacementResponseStorage(self, value: DisplacementResponseStorage):
        """Set displacementResponseStorage"""
        self.__displacementResponseStorage = value

    @property
    def forceResponseStorage(self) -> ForceResponseStorage:
        """"""
        return self.__forceResponseStorage

    @forceResponseStorage.setter
    def forceResponseStorage(self, value: ForceResponseStorage):
        """Set forceResponseStorage"""
        self.__forceResponseStorage = value

    @property
    def sumForceResponseStorage(self) -> SumForceResponseStorage:
        """"""
        return self.__sumForceResponseStorage

    @sumForceResponseStorage.setter
    def sumForceResponseStorage(self, value: SumForceResponseStorage):
        """Set sumForceResponseStorage"""
        self.__sumForceResponseStorage = value

    @property
    def curvatureResponseStorage(self) -> CurvatureResponseStorage:
        """"""
        return self.__curvatureResponseStorage

    @curvatureResponseStorage.setter
    def curvatureResponseStorage(self, value: CurvatureResponseStorage):
        """Set curvatureResponseStorage"""
        self.__curvatureResponseStorage = value

    @property
    def stressStorage(self) -> StressStorage:
        """"""
        return self.__stressStorage

    @stressStorage.setter
    def stressStorage(self, value: StressStorage):
        """Set stressStorage"""
        self.__stressStorage = value

    @property
    def turbineResponseStorage(self) -> TurbineResponseStorage:
        """"""
        return self.__turbineResponseStorage

    @turbineResponseStorage.setter
    def turbineResponseStorage(self, value: TurbineResponseStorage):
        """Set turbineResponseStorage"""
        self.__turbineResponseStorage = value

    @property
    def turbineBladeResponseStorage(self) -> TurbineBladeResponseStorage:
        """"""
        return self.__turbineBladeResponseStorage

    @turbineBladeResponseStorage.setter
    def turbineBladeResponseStorage(self, value: TurbineBladeResponseStorage):
        """Set turbineBladeResponseStorage"""
        self.__turbineBladeResponseStorage = value

    @property
    def supportVesselForceStorage(self) -> SupportVesselForceStorage:
        """"""
        return self.__supportVesselForceStorage

    @supportVesselForceStorage.setter
    def supportVesselForceStorage(self, value: SupportVesselForceStorage):
        """Set supportVesselForceStorage"""
        self.__supportVesselForceStorage = value

    @property
    def bodyForceStorage(self) -> BodyForceStorage:
        """"""
        return self.__bodyForceStorage

    @bodyForceStorage.setter
    def bodyForceStorage(self, value: BodyForceStorage):
        """Set bodyForceStorage"""
        self.__bodyForceStorage = value

    @property
    def hydrodynamicLoadStorage(self) -> HydrodynamicLoadStorage:
        """"""
        return self.__hydrodynamicLoadStorage

    @hydrodynamicLoadStorage.setter
    def hydrodynamicLoadStorage(self, value: HydrodynamicLoadStorage):
        """Set hydrodynamicLoadStorage"""
        self.__hydrodynamicLoadStorage = value

    @property
    def hlaElementForces(self) -> List[HLAElementForce]:
        """"""
        return self.__hlaElementForces

    @hlaElementForces.setter
    def hlaElementForces(self, value: List[HLAElementForce]):
        """Set hlaElementForces"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__hlaElementForces = value

    @property
    def hlaImportedBodies(self) -> List[ImportVesselItem]:
        """"""
        return self.__hlaImportedBodies

    @hlaImportedBodies.setter
    def hlaImportedBodies(self, value: List[ImportVesselItem]):
        """Set hlaImportedBodies"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__hlaImportedBodies = value

    @property
    def segmentLengthVariations(self) -> List[SegmentLengthVariationItem]:
        """"""
        return self.__segmentLengthVariations

    @segmentLengthVariations.setter
    def segmentLengthVariations(self, value: List[SegmentLengthVariationItem]):
        """Set segmentLengthVariations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__segmentLengthVariations = value

    @property
    def temperatureVariations(self) -> List[DynamicTemperatureVariationItem]:
        """"""
        return self.__temperatureVariations

    @temperatureVariations.setter
    def temperatureVariations(self, value: List[DynamicTemperatureVariationItem]):
        """Set temperatureVariations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__temperatureVariations = value

    @property
    def pressureVariations(self) -> List[DynamicPressureVariationItem]:
        """"""
        return self.__pressureVariations

    @pressureVariations.setter
    def pressureVariations(self, value: List[DynamicPressureVariationItem]):
        """Set pressureVariations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__pressureVariations = value

    @property
    def winchVariations(self) -> List[DynamicWinchVariationItem]:
        """"""
        return self.__winchVariations

    @winchVariations.setter
    def winchVariations(self, value: List[DynamicWinchVariationItem]):
        """Set winchVariations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__winchVariations = value

    @property
    def dynamicWindChange(self) -> DynamicWindChange:
        """"""
        return self.__dynamicWindChange

    @dynamicWindChange.setter
    def dynamicWindChange(self, value: DynamicWindChange):
        """Set dynamicWindChange"""
        self.__dynamicWindChange = value

    @property
    def windTurbineShutdown(self) -> WindTurbineShutdown:
        """"""
        return self.__windTurbineShutdown

    @windTurbineShutdown.setter
    def windTurbineShutdown(self, value: WindTurbineShutdown):
        """Set windTurbineShutdown"""
        self.__windTurbineShutdown = value

    @property
    def bladePitchFault(self) -> BladePitchFault:
        """"""
        return self.__bladePitchFault

    @bladePitchFault.setter
    def bladePitchFault(self, value: BladePitchFault):
        """Set bladePitchFault"""
        self.__bladePitchFault = value

    @property
    def boundaryChangeGroups(self) -> List[BoundaryChangeGroup]:
        """"""
        return self.__boundaryChangeGroups

    @boundaryChangeGroups.setter
    def boundaryChangeGroups(self, value: List[BoundaryChangeGroup]):
        """Set boundaryChangeGroups"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__boundaryChangeGroups = value

    @property
    def visualisationResponses(self) -> DynmodVisualisationResponses:
        """"""
        return self.__visualisationResponses

    @visualisationResponses.setter
    def visualisationResponses(self, value: DynmodVisualisationResponses):
        """Set visualisationResponses"""
        self.__visualisationResponses = value

    @property
    def regularWaveAnalysis(self) -> RegularWaveAnalaysis:
        """"""
        return self.__regularWaveAnalysis

    @regularWaveAnalysis.setter
    def regularWaveAnalysis(self, value: RegularWaveAnalaysis):
        """Set regularWaveAnalysis"""
        self.__regularWaveAnalysis = value

    @property
    def regularWaveLoading(self) -> RegularWaveLoading:
        """"""
        return self.__regularWaveLoading

    @regularWaveLoading.setter
    def regularWaveLoading(self, value: RegularWaveLoading):
        """Set regularWaveLoading"""
        self.__regularWaveLoading = value

    @property
    def regularVesselMotions(self) -> List[RegularVesselMotion]:
        """"""
        return self.__regularVesselMotions

    @regularVesselMotions.setter
    def regularVesselMotions(self, value: List[RegularVesselMotion]):
        """Set regularVesselMotions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__regularVesselMotions = value

    @property
    def volumeForcesScaling(self) -> float:
        """Scaling of volume forces."""
        return self.__volumeForcesScaling

    @volumeForcesScaling.setter
    def volumeForcesScaling(self, value: float):
        """Set volumeForcesScaling"""
        self.__volumeForcesScaling = float(value)

    @property
    def specifiedForcesScaling(self) -> float:
        """Scaling of specified (nodal) forces."""
        return self.__specifiedForcesScaling

    @specifiedForcesScaling.setter
    def specifiedForcesScaling(self, value: float):
        """Set specifiedForcesScaling"""
        self.__specifiedForcesScaling = float(value)

    @property
    def currentVelocitiesScaling(self) -> float:
        """Scaling of current velocities."""
        return self.__currentVelocitiesScaling

    @currentVelocitiesScaling.setter
    def currentVelocitiesScaling(self, value: float):
        """Set currentVelocitiesScaling"""
        self.__currentVelocitiesScaling = float(value)

    @property
    def changeStaticLoads(self) -> bool:
        """Change applied static loads at the start of the dynamic analysis"""
        return self.__changeStaticLoads

    @changeStaticLoads.setter
    def changeStaticLoads(self, value: bool):
        """Set changeStaticLoads"""
        self.__changeStaticLoads = bool(value)

    @property
    def dynamicLoads(self) -> DynamicLoads:
        """"""
        return self.__dynamicLoads

    @dynamicLoads.setter
    def dynamicLoads(self, value: DynamicLoads):
        """Set dynamicLoads"""
        self.__dynamicLoads = value

    @property
    def bottomContactStorage(self) -> BottomContactStorage:
        """"""
        return self.__bottomContactStorage

    @bottomContactStorage.setter
    def bottomContactStorage(self, value: BottomContactStorage):
        """Set bottomContactStorage"""
        self.__bottomContactStorage = value

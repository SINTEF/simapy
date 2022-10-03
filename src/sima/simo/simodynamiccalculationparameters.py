# This an autogenerated file
# 
# Generated with SIMODynamicCalculationParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simodynamiccalculationparameters import SIMODynamicCalculationParametersBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.bodywavemethodoption import BodyWaveMethodOption
from sima.simo.currentforcemethod import CurrentForceMethod
from sima.simo.externalcontrolsetup import ExternalControlSetup
from sima.simo.hydrosystemfiltermethod import HydroSystemFilterMethod
from sima.simo.integrationmethod import IntegrationMethod
from sima.simo.multienvironmentsetup import MultiEnvironmentSetup
from sima.simo.randomgenerator import RandomGenerator
from sima.simo.wasimresultexport import WasimResultExport
from sima.simo.wavemethod import WaveMethod
from sima.simo.wavetimeseries import WaveTimeSeries
from sima.simo.windforcemethod import WindForceMethod
from sima.simo.windmethod import WindMethod
from sima.simo.windspectrumverticaldomain import WindSpectrumVerticalDomain
from sima.simo.windtimeseriesmethod import WindTimeSeriesMethod
from sima.simo.windvelocitydimension import WindVelocityDimension

class SIMODynamicCalculationParameters(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    externalControlSetup : ExternalControlSetup
    multiEnvironmentSetup : MultiEnvironmentSetup
    timeIncrement : float
         Time increment for time series generation and storage(default 0.5)
    waveMethod : WaveMethod
         Selected wave method
    integrationMethod : IntegrationMethod
         Selected integration method
    randomSeedWaves : int
         Random seed waves(default 1)
    randomSeedWind : int
         Random seed wind(default 1)
    randomGenerator : RandomGenerator
    headingCorrection : bool
         Use correction due to heading change(default True)
    maxHeadingChange : float
         Max heading change(default 45.0)
    largePatchLength : float
         Large visualization wave patch length(default 2048.0)
    smallPatchLength : float
         Small visualization wave patch length(default 256.0)
    cutFactorWaves : int
         Cut factor for wave components(default 100)
    pointsLargePatch : int
         Number of points in large wave patch(default 256)
    pointsSmallPatch : int
         Number of points in small wave patch(default 128)
    writeVisFile : bool
         write visualization file?(default True)
    waveTimeSeries : WaveTimeSeries
    waveTimeSeriesFile : bool
         Wave time series from file(default True)
    bodyWaveMethodOptions : List[BodyWaveMethodOption]
    hydroSystemPeriod : float
         Hydrosystem filter period(default 0.0)
    hydroFilterMethod : HydroSystemFilterMethod
         Hydro Filter Method
    nWindSeaComponents : int
         Number of wind-sea components(default 2000)
    nSwellSeaComponents : int
         Number of wind-sea components(default 400)
    windTimeSeriesMethod : WindTimeSeriesMethod
         Wind Time Series Method
    windVelocityDimension : WindVelocityDimension
         Wind Velocity Dimension
    windForceMethod : WindForceMethod
         Wind Force Method
    windMethod : WindMethod
    windSpectrumVerticalDomain : WindSpectrumVerticalDomain
    quadraticCurrentForceMethod : CurrentForceMethod
         Quadratic Current Force Method
    linearCurrentForceMethod : CurrentForceMethod
         Linear Current Force Method
    exportResultsToWasim : bool
         (default True)
    wasimResultExport : WasimResultExport
    storeWindForces : bool
         Store wind forces?(default True)
    storeSumGeneralLineForces : bool
         Store sum general line forces?(default True)
    storeTotalForces : bool
         Store total forces?(default True)
    storeRetardationForces : bool
         Store retardation forces?(default True)
    storeHydrostaticStiffnessForces : bool
         Store hydrostatic stiffness forces?(default True)
    storeLinearDamping : bool
         Store linear damping?(default True)
    storeQuadraticDamping : bool
         Store quadratic damping?(default True)
    storeDistributedHydrodynamicForces : bool
         Store distributed hydrodynamic forces?(default True)
    storeFixedBodyAndSlenderElementStripResults : bool
         Store results for slender element strips and fixed body elements?(default True)
    storeWaveDriftDamping : bool
         Store wave-drift damping?(default True)
    storeLinearCurrentDrag : bool
         Store linear current drag?(default True)
    storeQuadraticCurrentDrag : bool
         Store quadratic current drag?(default True)
    storeSmallBodyHydrodynamicForces : bool
         Store small body hydrodynamic forces?(default True)
    storeResultantPositioningElementForces : bool
         Store resultant positioning element forces?(default True)
    storePositioningElementForceComponents : bool
         Store positioning element force components?(default True)
    storeTotalPositioningForces : bool
         Store total positioning element forces?(default True)
    storeThrusterForces : bool
         Store thruster forces?(default True)
    storeSumThrusterForces : bool
         Store sum thruster forces?(default True)
    storeDynamicPositioningEstimators : bool
         Store dynamic positioning estimators?(default True)
    storeSumSpecifiedForces : bool
         Store sum specified forces?(default True)
    storeSumExternalForces : bool
         Store sum external forces?(default True)
    storeSumCouplingForces : bool
         Store sum coupling forces?(default True)
    storeResultantCouplingElementForces : bool
         Store resultant coupling element forces?(default True)
    storeGlobalCouplingForceComponents : bool
         Store global coupling force components?(default True)
    storeLocalCouplingForceComponents : bool
         Store local coupling force components?(default True)
    storeGlobalLowFrequencyPosition : bool
         Store global low-frequency position?(default True)
    storeGlobalTotalPosition : bool
         Store global total position?(default True)
    storeGlobalAcceleration : bool
         Store global acceleration?(default True)
    storeLocalAccelerations : bool
         Store local acceleration?(default True)
    storeLocalVelocity : bool
         Store local velocity(default True)
    storeCatenarySystemForces : bool
         Store catenery system forces. Requires visualization storage(default True)
    storeCatenarySystemNodes : bool
         Store displacement of catenary system nodes. Requires visualization storage(default True)
    timeStep : float
         Time integration step(default 0.5)
    simulationLength : float
         Simulation length(default 11000.0)
    simulationStartTime : float
         Time (in generated time series) that dynamic simulation will start from(default 0.0)
    rampDuration : float
         Determines the ramp duration in seconds(default 2.5)
    requestedTimeSeriesLength : float
         Length of generated time series(default 16384.0)
    """

    def __init__(self , _id="", timeIncrement=0.5, waveMethod=WaveMethod.FFT_ONLY, integrationMethod=IntegrationMethod.RUNGE_KUTTA, randomSeedWaves=1, randomSeedWind=1, randomGenerator=RandomGenerator.LEGACY, headingCorrection=True, maxHeadingChange=45.0, largePatchLength=2048.0, smallPatchLength=256.0, cutFactorWaves=100, pointsLargePatch=256, pointsSmallPatch=128, writeVisFile=True, waveTimeSeriesFile=True, hydroSystemPeriod=0.0, hydroFilterMethod=HydroSystemFilterMethod.BLOCKED, nWindSeaComponents=2000, nSwellSeaComponents=400, windTimeSeriesMethod=WindTimeSeriesMethod.SAME, windVelocityDimension=WindVelocityDimension.TWO, windForceMethod=WindForceMethod.RELATIVE, windMethod=WindMethod.FFT, quadraticCurrentForceMethod=CurrentForceMethod.RELATIVE, linearCurrentForceMethod=CurrentForceMethod.RELATIVE, exportResultsToWasim=True, storeWindForces=True, storeSumGeneralLineForces=True, storeTotalForces=True, storeRetardationForces=True, storeHydrostaticStiffnessForces=True, storeLinearDamping=True, storeQuadraticDamping=True, storeDistributedHydrodynamicForces=True, storeFixedBodyAndSlenderElementStripResults=True, storeWaveDriftDamping=True, storeLinearCurrentDrag=True, storeQuadraticCurrentDrag=True, storeSmallBodyHydrodynamicForces=True, storeResultantPositioningElementForces=True, storePositioningElementForceComponents=True, storeTotalPositioningForces=True, storeThrusterForces=True, storeSumThrusterForces=True, storeDynamicPositioningEstimators=True, storeSumSpecifiedForces=True, storeSumExternalForces=True, storeSumCouplingForces=True, storeResultantCouplingElementForces=True, storeGlobalCouplingForceComponents=True, storeLocalCouplingForceComponents=True, storeGlobalLowFrequencyPosition=True, storeGlobalTotalPosition=True, storeGlobalAcceleration=True, storeLocalAccelerations=True, storeLocalVelocity=True, storeCatenarySystemForces=True, storeCatenarySystemNodes=True, timeStep=0.5, simulationLength=11000.0, simulationStartTime=0.0, rampDuration=2.5, requestedTimeSeriesLength=16384.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.externalControlSetup = None
        self.multiEnvironmentSetup = None
        self.timeIncrement = timeIncrement
        self.waveMethod = waveMethod
        self.integrationMethod = integrationMethod
        self.randomSeedWaves = randomSeedWaves
        self.randomSeedWind = randomSeedWind
        self.randomGenerator = randomGenerator
        self.headingCorrection = headingCorrection
        self.maxHeadingChange = maxHeadingChange
        self.largePatchLength = largePatchLength
        self.smallPatchLength = smallPatchLength
        self.cutFactorWaves = cutFactorWaves
        self.pointsLargePatch = pointsLargePatch
        self.pointsSmallPatch = pointsSmallPatch
        self.writeVisFile = writeVisFile
        self.waveTimeSeries = None
        self.waveTimeSeriesFile = waveTimeSeriesFile
        self.bodyWaveMethodOptions = list()
        self.hydroSystemPeriod = hydroSystemPeriod
        self.hydroFilterMethod = hydroFilterMethod
        self.nWindSeaComponents = nWindSeaComponents
        self.nSwellSeaComponents = nSwellSeaComponents
        self.windTimeSeriesMethod = windTimeSeriesMethod
        self.windVelocityDimension = windVelocityDimension
        self.windForceMethod = windForceMethod
        self.windMethod = windMethod
        self.windSpectrumVerticalDomain = None
        self.quadraticCurrentForceMethod = quadraticCurrentForceMethod
        self.linearCurrentForceMethod = linearCurrentForceMethod
        self.exportResultsToWasim = exportResultsToWasim
        self.wasimResultExport = None
        self.storeWindForces = storeWindForces
        self.storeSumGeneralLineForces = storeSumGeneralLineForces
        self.storeTotalForces = storeTotalForces
        self.storeRetardationForces = storeRetardationForces
        self.storeHydrostaticStiffnessForces = storeHydrostaticStiffnessForces
        self.storeLinearDamping = storeLinearDamping
        self.storeQuadraticDamping = storeQuadraticDamping
        self.storeDistributedHydrodynamicForces = storeDistributedHydrodynamicForces
        self.storeFixedBodyAndSlenderElementStripResults = storeFixedBodyAndSlenderElementStripResults
        self.storeWaveDriftDamping = storeWaveDriftDamping
        self.storeLinearCurrentDrag = storeLinearCurrentDrag
        self.storeQuadraticCurrentDrag = storeQuadraticCurrentDrag
        self.storeSmallBodyHydrodynamicForces = storeSmallBodyHydrodynamicForces
        self.storeResultantPositioningElementForces = storeResultantPositioningElementForces
        self.storePositioningElementForceComponents = storePositioningElementForceComponents
        self.storeTotalPositioningForces = storeTotalPositioningForces
        self.storeThrusterForces = storeThrusterForces
        self.storeSumThrusterForces = storeSumThrusterForces
        self.storeDynamicPositioningEstimators = storeDynamicPositioningEstimators
        self.storeSumSpecifiedForces = storeSumSpecifiedForces
        self.storeSumExternalForces = storeSumExternalForces
        self.storeSumCouplingForces = storeSumCouplingForces
        self.storeResultantCouplingElementForces = storeResultantCouplingElementForces
        self.storeGlobalCouplingForceComponents = storeGlobalCouplingForceComponents
        self.storeLocalCouplingForceComponents = storeLocalCouplingForceComponents
        self.storeGlobalLowFrequencyPosition = storeGlobalLowFrequencyPosition
        self.storeGlobalTotalPosition = storeGlobalTotalPosition
        self.storeGlobalAcceleration = storeGlobalAcceleration
        self.storeLocalAccelerations = storeLocalAccelerations
        self.storeLocalVelocity = storeLocalVelocity
        self.storeCatenarySystemForces = storeCatenarySystemForces
        self.storeCatenarySystemNodes = storeCatenarySystemNodes
        self.timeStep = timeStep
        self.simulationLength = simulationLength
        self.simulationStartTime = simulationStartTime
        self.rampDuration = rampDuration
        self.requestedTimeSeriesLength = requestedTimeSeriesLength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMODynamicCalculationParametersBlueprint()


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
    def externalControlSetup(self) -> ExternalControlSetup:
        """"""
        return self.__externalControlSetup

    @externalControlSetup.setter
    def externalControlSetup(self, value: ExternalControlSetup):
        """Set externalControlSetup"""
        self.__externalControlSetup = value

    @property
    def multiEnvironmentSetup(self) -> MultiEnvironmentSetup:
        """"""
        return self.__multiEnvironmentSetup

    @multiEnvironmentSetup.setter
    def multiEnvironmentSetup(self, value: MultiEnvironmentSetup):
        """Set multiEnvironmentSetup"""
        self.__multiEnvironmentSetup = value

    @property
    def timeIncrement(self) -> float:
        """Time increment for time series generation and storage"""
        return self.__timeIncrement

    @timeIncrement.setter
    def timeIncrement(self, value: float):
        """Set timeIncrement"""
        self.__timeIncrement = float(value)

    @property
    def waveMethod(self) -> WaveMethod:
        """Selected wave method"""
        return self.__waveMethod

    @waveMethod.setter
    def waveMethod(self, value: WaveMethod):
        """Set waveMethod"""
        self.__waveMethod = value

    @property
    def integrationMethod(self) -> IntegrationMethod:
        """Selected integration method"""
        return self.__integrationMethod

    @integrationMethod.setter
    def integrationMethod(self, value: IntegrationMethod):
        """Set integrationMethod"""
        self.__integrationMethod = value

    @property
    def randomSeedWaves(self) -> int:
        """Random seed waves"""
        return self.__randomSeedWaves

    @randomSeedWaves.setter
    def randomSeedWaves(self, value: int):
        """Set randomSeedWaves"""
        self.__randomSeedWaves = int(value)

    @property
    def randomSeedWind(self) -> int:
        """Random seed wind"""
        return self.__randomSeedWind

    @randomSeedWind.setter
    def randomSeedWind(self, value: int):
        """Set randomSeedWind"""
        self.__randomSeedWind = int(value)

    @property
    def randomGenerator(self) -> RandomGenerator:
        """"""
        return self.__randomGenerator

    @randomGenerator.setter
    def randomGenerator(self, value: RandomGenerator):
        """Set randomGenerator"""
        self.__randomGenerator = value

    @property
    def headingCorrection(self) -> bool:
        """Use correction due to heading change"""
        return self.__headingCorrection

    @headingCorrection.setter
    def headingCorrection(self, value: bool):
        """Set headingCorrection"""
        self.__headingCorrection = bool(value)

    @property
    def maxHeadingChange(self) -> float:
        """Max heading change"""
        return self.__maxHeadingChange

    @maxHeadingChange.setter
    def maxHeadingChange(self, value: float):
        """Set maxHeadingChange"""
        self.__maxHeadingChange = float(value)

    @property
    def largePatchLength(self) -> float:
        """Large visualization wave patch length"""
        return self.__largePatchLength

    @largePatchLength.setter
    def largePatchLength(self, value: float):
        """Set largePatchLength"""
        self.__largePatchLength = float(value)

    @property
    def smallPatchLength(self) -> float:
        """Small visualization wave patch length"""
        return self.__smallPatchLength

    @smallPatchLength.setter
    def smallPatchLength(self, value: float):
        """Set smallPatchLength"""
        self.__smallPatchLength = float(value)

    @property
    def cutFactorWaves(self) -> int:
        """Cut factor for wave components"""
        return self.__cutFactorWaves

    @cutFactorWaves.setter
    def cutFactorWaves(self, value: int):
        """Set cutFactorWaves"""
        self.__cutFactorWaves = int(value)

    @property
    def pointsLargePatch(self) -> int:
        """Number of points in large wave patch"""
        return self.__pointsLargePatch

    @pointsLargePatch.setter
    def pointsLargePatch(self, value: int):
        """Set pointsLargePatch"""
        self.__pointsLargePatch = int(value)

    @property
    def pointsSmallPatch(self) -> int:
        """Number of points in small wave patch"""
        return self.__pointsSmallPatch

    @pointsSmallPatch.setter
    def pointsSmallPatch(self, value: int):
        """Set pointsSmallPatch"""
        self.__pointsSmallPatch = int(value)

    @property
    def writeVisFile(self) -> bool:
        """write visualization file?"""
        return self.__writeVisFile

    @writeVisFile.setter
    def writeVisFile(self, value: bool):
        """Set writeVisFile"""
        self.__writeVisFile = bool(value)

    @property
    def waveTimeSeries(self) -> WaveTimeSeries:
        """"""
        return self.__waveTimeSeries

    @waveTimeSeries.setter
    def waveTimeSeries(self, value: WaveTimeSeries):
        """Set waveTimeSeries"""
        self.__waveTimeSeries = value

    @property
    def waveTimeSeriesFile(self) -> bool:
        """Wave time series from file"""
        return self.__waveTimeSeriesFile

    @waveTimeSeriesFile.setter
    def waveTimeSeriesFile(self, value: bool):
        """Set waveTimeSeriesFile"""
        self.__waveTimeSeriesFile = bool(value)

    @property
    def bodyWaveMethodOptions(self) -> List[BodyWaveMethodOption]:
        """"""
        return self.__bodyWaveMethodOptions

    @bodyWaveMethodOptions.setter
    def bodyWaveMethodOptions(self, value: List[BodyWaveMethodOption]):
        """Set bodyWaveMethodOptions"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__bodyWaveMethodOptions = value

    @property
    def hydroSystemPeriod(self) -> float:
        """Hydrosystem filter period"""
        return self.__hydroSystemPeriod

    @hydroSystemPeriod.setter
    def hydroSystemPeriod(self, value: float):
        """Set hydroSystemPeriod"""
        self.__hydroSystemPeriod = float(value)

    @property
    def hydroFilterMethod(self) -> HydroSystemFilterMethod:
        """Hydro Filter Method"""
        return self.__hydroFilterMethod

    @hydroFilterMethod.setter
    def hydroFilterMethod(self, value: HydroSystemFilterMethod):
        """Set hydroFilterMethod"""
        self.__hydroFilterMethod = value

    @property
    def nWindSeaComponents(self) -> int:
        """Number of wind-sea components"""
        return self.__nWindSeaComponents

    @nWindSeaComponents.setter
    def nWindSeaComponents(self, value: int):
        """Set nWindSeaComponents"""
        self.__nWindSeaComponents = int(value)

    @property
    def nSwellSeaComponents(self) -> int:
        """Number of wind-sea components"""
        return self.__nSwellSeaComponents

    @nSwellSeaComponents.setter
    def nSwellSeaComponents(self, value: int):
        """Set nSwellSeaComponents"""
        self.__nSwellSeaComponents = int(value)

    @property
    def windTimeSeriesMethod(self) -> WindTimeSeriesMethod:
        """Wind Time Series Method"""
        return self.__windTimeSeriesMethod

    @windTimeSeriesMethod.setter
    def windTimeSeriesMethod(self, value: WindTimeSeriesMethod):
        """Set windTimeSeriesMethod"""
        self.__windTimeSeriesMethod = value

    @property
    def windVelocityDimension(self) -> WindVelocityDimension:
        """Wind Velocity Dimension"""
        return self.__windVelocityDimension

    @windVelocityDimension.setter
    def windVelocityDimension(self, value: WindVelocityDimension):
        """Set windVelocityDimension"""
        self.__windVelocityDimension = value

    @property
    def windForceMethod(self) -> WindForceMethod:
        """Wind Force Method"""
        return self.__windForceMethod

    @windForceMethod.setter
    def windForceMethod(self, value: WindForceMethod):
        """Set windForceMethod"""
        self.__windForceMethod = value

    @property
    def windMethod(self) -> WindMethod:
        """"""
        return self.__windMethod

    @windMethod.setter
    def windMethod(self, value: WindMethod):
        """Set windMethod"""
        self.__windMethod = value

    @property
    def windSpectrumVerticalDomain(self) -> WindSpectrumVerticalDomain:
        """"""
        return self.__windSpectrumVerticalDomain

    @windSpectrumVerticalDomain.setter
    def windSpectrumVerticalDomain(self, value: WindSpectrumVerticalDomain):
        """Set windSpectrumVerticalDomain"""
        self.__windSpectrumVerticalDomain = value

    @property
    def quadraticCurrentForceMethod(self) -> CurrentForceMethod:
        """Quadratic Current Force Method"""
        return self.__quadraticCurrentForceMethod

    @quadraticCurrentForceMethod.setter
    def quadraticCurrentForceMethod(self, value: CurrentForceMethod):
        """Set quadraticCurrentForceMethod"""
        self.__quadraticCurrentForceMethod = value

    @property
    def linearCurrentForceMethod(self) -> CurrentForceMethod:
        """Linear Current Force Method"""
        return self.__linearCurrentForceMethod

    @linearCurrentForceMethod.setter
    def linearCurrentForceMethod(self, value: CurrentForceMethod):
        """Set linearCurrentForceMethod"""
        self.__linearCurrentForceMethod = value

    @property
    def exportResultsToWasim(self) -> bool:
        """"""
        return self.__exportResultsToWasim

    @exportResultsToWasim.setter
    def exportResultsToWasim(self, value: bool):
        """Set exportResultsToWasim"""
        self.__exportResultsToWasim = bool(value)

    @property
    def wasimResultExport(self) -> WasimResultExport:
        """"""
        return self.__wasimResultExport

    @wasimResultExport.setter
    def wasimResultExport(self, value: WasimResultExport):
        """Set wasimResultExport"""
        self.__wasimResultExport = value

    @property
    def storeWindForces(self) -> bool:
        """Store wind forces?"""
        return self.__storeWindForces

    @storeWindForces.setter
    def storeWindForces(self, value: bool):
        """Set storeWindForces"""
        self.__storeWindForces = bool(value)

    @property
    def storeSumGeneralLineForces(self) -> bool:
        """Store sum general line forces?"""
        return self.__storeSumGeneralLineForces

    @storeSumGeneralLineForces.setter
    def storeSumGeneralLineForces(self, value: bool):
        """Set storeSumGeneralLineForces"""
        self.__storeSumGeneralLineForces = bool(value)

    @property
    def storeTotalForces(self) -> bool:
        """Store total forces?"""
        return self.__storeTotalForces

    @storeTotalForces.setter
    def storeTotalForces(self, value: bool):
        """Set storeTotalForces"""
        self.__storeTotalForces = bool(value)

    @property
    def storeRetardationForces(self) -> bool:
        """Store retardation forces?"""
        return self.__storeRetardationForces

    @storeRetardationForces.setter
    def storeRetardationForces(self, value: bool):
        """Set storeRetardationForces"""
        self.__storeRetardationForces = bool(value)

    @property
    def storeHydrostaticStiffnessForces(self) -> bool:
        """Store hydrostatic stiffness forces?"""
        return self.__storeHydrostaticStiffnessForces

    @storeHydrostaticStiffnessForces.setter
    def storeHydrostaticStiffnessForces(self, value: bool):
        """Set storeHydrostaticStiffnessForces"""
        self.__storeHydrostaticStiffnessForces = bool(value)

    @property
    def storeLinearDamping(self) -> bool:
        """Store linear damping?"""
        return self.__storeLinearDamping

    @storeLinearDamping.setter
    def storeLinearDamping(self, value: bool):
        """Set storeLinearDamping"""
        self.__storeLinearDamping = bool(value)

    @property
    def storeQuadraticDamping(self) -> bool:
        """Store quadratic damping?"""
        return self.__storeQuadraticDamping

    @storeQuadraticDamping.setter
    def storeQuadraticDamping(self, value: bool):
        """Set storeQuadraticDamping"""
        self.__storeQuadraticDamping = bool(value)

    @property
    def storeDistributedHydrodynamicForces(self) -> bool:
        """Store distributed hydrodynamic forces?"""
        return self.__storeDistributedHydrodynamicForces

    @storeDistributedHydrodynamicForces.setter
    def storeDistributedHydrodynamicForces(self, value: bool):
        """Set storeDistributedHydrodynamicForces"""
        self.__storeDistributedHydrodynamicForces = bool(value)

    @property
    def storeFixedBodyAndSlenderElementStripResults(self) -> bool:
        """Store results for slender element strips and fixed body elements?"""
        return self.__storeFixedBodyAndSlenderElementStripResults

    @storeFixedBodyAndSlenderElementStripResults.setter
    def storeFixedBodyAndSlenderElementStripResults(self, value: bool):
        """Set storeFixedBodyAndSlenderElementStripResults"""
        self.__storeFixedBodyAndSlenderElementStripResults = bool(value)

    @property
    def storeWaveDriftDamping(self) -> bool:
        """Store wave-drift damping?"""
        return self.__storeWaveDriftDamping

    @storeWaveDriftDamping.setter
    def storeWaveDriftDamping(self, value: bool):
        """Set storeWaveDriftDamping"""
        self.__storeWaveDriftDamping = bool(value)

    @property
    def storeLinearCurrentDrag(self) -> bool:
        """Store linear current drag?"""
        return self.__storeLinearCurrentDrag

    @storeLinearCurrentDrag.setter
    def storeLinearCurrentDrag(self, value: bool):
        """Set storeLinearCurrentDrag"""
        self.__storeLinearCurrentDrag = bool(value)

    @property
    def storeQuadraticCurrentDrag(self) -> bool:
        """Store quadratic current drag?"""
        return self.__storeQuadraticCurrentDrag

    @storeQuadraticCurrentDrag.setter
    def storeQuadraticCurrentDrag(self, value: bool):
        """Set storeQuadraticCurrentDrag"""
        self.__storeQuadraticCurrentDrag = bool(value)

    @property
    def storeSmallBodyHydrodynamicForces(self) -> bool:
        """Store small body hydrodynamic forces?"""
        return self.__storeSmallBodyHydrodynamicForces

    @storeSmallBodyHydrodynamicForces.setter
    def storeSmallBodyHydrodynamicForces(self, value: bool):
        """Set storeSmallBodyHydrodynamicForces"""
        self.__storeSmallBodyHydrodynamicForces = bool(value)

    @property
    def storeResultantPositioningElementForces(self) -> bool:
        """Store resultant positioning element forces?"""
        return self.__storeResultantPositioningElementForces

    @storeResultantPositioningElementForces.setter
    def storeResultantPositioningElementForces(self, value: bool):
        """Set storeResultantPositioningElementForces"""
        self.__storeResultantPositioningElementForces = bool(value)

    @property
    def storePositioningElementForceComponents(self) -> bool:
        """Store positioning element force components?"""
        return self.__storePositioningElementForceComponents

    @storePositioningElementForceComponents.setter
    def storePositioningElementForceComponents(self, value: bool):
        """Set storePositioningElementForceComponents"""
        self.__storePositioningElementForceComponents = bool(value)

    @property
    def storeTotalPositioningForces(self) -> bool:
        """Store total positioning element forces?"""
        return self.__storeTotalPositioningForces

    @storeTotalPositioningForces.setter
    def storeTotalPositioningForces(self, value: bool):
        """Set storeTotalPositioningForces"""
        self.__storeTotalPositioningForces = bool(value)

    @property
    def storeThrusterForces(self) -> bool:
        """Store thruster forces?"""
        return self.__storeThrusterForces

    @storeThrusterForces.setter
    def storeThrusterForces(self, value: bool):
        """Set storeThrusterForces"""
        self.__storeThrusterForces = bool(value)

    @property
    def storeSumThrusterForces(self) -> bool:
        """Store sum thruster forces?"""
        return self.__storeSumThrusterForces

    @storeSumThrusterForces.setter
    def storeSumThrusterForces(self, value: bool):
        """Set storeSumThrusterForces"""
        self.__storeSumThrusterForces = bool(value)

    @property
    def storeDynamicPositioningEstimators(self) -> bool:
        """Store dynamic positioning estimators?"""
        return self.__storeDynamicPositioningEstimators

    @storeDynamicPositioningEstimators.setter
    def storeDynamicPositioningEstimators(self, value: bool):
        """Set storeDynamicPositioningEstimators"""
        self.__storeDynamicPositioningEstimators = bool(value)

    @property
    def storeSumSpecifiedForces(self) -> bool:
        """Store sum specified forces?"""
        return self.__storeSumSpecifiedForces

    @storeSumSpecifiedForces.setter
    def storeSumSpecifiedForces(self, value: bool):
        """Set storeSumSpecifiedForces"""
        self.__storeSumSpecifiedForces = bool(value)

    @property
    def storeSumExternalForces(self) -> bool:
        """Store sum external forces?"""
        return self.__storeSumExternalForces

    @storeSumExternalForces.setter
    def storeSumExternalForces(self, value: bool):
        """Set storeSumExternalForces"""
        self.__storeSumExternalForces = bool(value)

    @property
    def storeSumCouplingForces(self) -> bool:
        """Store sum coupling forces?"""
        return self.__storeSumCouplingForces

    @storeSumCouplingForces.setter
    def storeSumCouplingForces(self, value: bool):
        """Set storeSumCouplingForces"""
        self.__storeSumCouplingForces = bool(value)

    @property
    def storeResultantCouplingElementForces(self) -> bool:
        """Store resultant coupling element forces?"""
        return self.__storeResultantCouplingElementForces

    @storeResultantCouplingElementForces.setter
    def storeResultantCouplingElementForces(self, value: bool):
        """Set storeResultantCouplingElementForces"""
        self.__storeResultantCouplingElementForces = bool(value)

    @property
    def storeGlobalCouplingForceComponents(self) -> bool:
        """Store global coupling force components?"""
        return self.__storeGlobalCouplingForceComponents

    @storeGlobalCouplingForceComponents.setter
    def storeGlobalCouplingForceComponents(self, value: bool):
        """Set storeGlobalCouplingForceComponents"""
        self.__storeGlobalCouplingForceComponents = bool(value)

    @property
    def storeLocalCouplingForceComponents(self) -> bool:
        """Store local coupling force components?"""
        return self.__storeLocalCouplingForceComponents

    @storeLocalCouplingForceComponents.setter
    def storeLocalCouplingForceComponents(self, value: bool):
        """Set storeLocalCouplingForceComponents"""
        self.__storeLocalCouplingForceComponents = bool(value)

    @property
    def storeGlobalLowFrequencyPosition(self) -> bool:
        """Store global low-frequency position?"""
        return self.__storeGlobalLowFrequencyPosition

    @storeGlobalLowFrequencyPosition.setter
    def storeGlobalLowFrequencyPosition(self, value: bool):
        """Set storeGlobalLowFrequencyPosition"""
        self.__storeGlobalLowFrequencyPosition = bool(value)

    @property
    def storeGlobalTotalPosition(self) -> bool:
        """Store global total position?"""
        return self.__storeGlobalTotalPosition

    @storeGlobalTotalPosition.setter
    def storeGlobalTotalPosition(self, value: bool):
        """Set storeGlobalTotalPosition"""
        self.__storeGlobalTotalPosition = bool(value)

    @property
    def storeGlobalAcceleration(self) -> bool:
        """Store global acceleration?"""
        return self.__storeGlobalAcceleration

    @storeGlobalAcceleration.setter
    def storeGlobalAcceleration(self, value: bool):
        """Set storeGlobalAcceleration"""
        self.__storeGlobalAcceleration = bool(value)

    @property
    def storeLocalAccelerations(self) -> bool:
        """Store local acceleration?"""
        return self.__storeLocalAccelerations

    @storeLocalAccelerations.setter
    def storeLocalAccelerations(self, value: bool):
        """Set storeLocalAccelerations"""
        self.__storeLocalAccelerations = bool(value)

    @property
    def storeLocalVelocity(self) -> bool:
        """Store local velocity"""
        return self.__storeLocalVelocity

    @storeLocalVelocity.setter
    def storeLocalVelocity(self, value: bool):
        """Set storeLocalVelocity"""
        self.__storeLocalVelocity = bool(value)

    @property
    def storeCatenarySystemForces(self) -> bool:
        """Store catenery system forces. Requires visualization storage"""
        return self.__storeCatenarySystemForces

    @storeCatenarySystemForces.setter
    def storeCatenarySystemForces(self, value: bool):
        """Set storeCatenarySystemForces"""
        self.__storeCatenarySystemForces = bool(value)

    @property
    def storeCatenarySystemNodes(self) -> bool:
        """Store displacement of catenary system nodes. Requires visualization storage"""
        return self.__storeCatenarySystemNodes

    @storeCatenarySystemNodes.setter
    def storeCatenarySystemNodes(self, value: bool):
        """Set storeCatenarySystemNodes"""
        self.__storeCatenarySystemNodes = bool(value)

    @property
    def timeStep(self) -> float:
        """Time integration step"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def simulationLength(self) -> float:
        """Simulation length"""
        return self.__simulationLength

    @simulationLength.setter
    def simulationLength(self, value: float):
        """Set simulationLength"""
        self.__simulationLength = float(value)

    @property
    def simulationStartTime(self) -> float:
        """Time (in generated time series) that dynamic simulation will start from"""
        return self.__simulationStartTime

    @simulationStartTime.setter
    def simulationStartTime(self, value: float):
        """Set simulationStartTime"""
        self.__simulationStartTime = float(value)

    @property
    def rampDuration(self) -> float:
        """Determines the ramp duration in seconds"""
        return self.__rampDuration

    @rampDuration.setter
    def rampDuration(self, value: float):
        """Set rampDuration"""
        self.__rampDuration = float(value)

    @property
    def requestedTimeSeriesLength(self) -> float:
        """Length of generated time series"""
        return self.__requestedTimeSeriesLength

    @requestedTimeSeriesLength.setter
    def requestedTimeSeriesLength(self, value: float):
        """Set requestedTimeSeriesLength"""
        self.__requestedTimeSeriesLength = float(value)

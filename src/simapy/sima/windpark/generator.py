# This an autogenerated file
# 
# Generated with Generator
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.generator import GeneratorBlueprint
from typing import Dict
from ..sima import ConditionSelectable
from ..sima import Named
from ..sima import ScriptableValue
from .areaaveragingoption import AreaAveragingOption
from .deficitanalysisoption import DeficitAnalysisOption
from .deficitfilecontents import DeficitFileContents
from .fileformat import FileFormat
from .filterlengthoption import FilterLengthOption
from .focus import Focus
from .incomingwind import IncomingWind
from .lowpassfrequencyoption import LowPassFrequencyOption
from .meanderinganalysisoption import MeanderingAnalysisOption
from .multipledeficitmethod import MultipleDeficitMethod
from .nearwakelengthmodel import NearWakeLengthModel
from .poweroption import PowerOption
from .shaftdirection import ShaftDirection
from .stabilityclass import StabilityClass
from .turbulenceboxoption import TurbulenceBoxOption
from .turbulenceboxscaling import TurbulenceBoxScaling
from .viscosityfilter import ViscosityFilter
from .wakeflowmodel import WakeFlowModel
from .weightoption import WeightOption
from .windparkturbine import WindParkTurbine
from .windturbinemotion import WindTurbineMotion
from .windturbinetype import WindTurbineType

class Generator(Named,ConditionSelectable):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    airDensity : float
         (default 1.3)
    kinematicViscosity : float
         (default 1.824e-05)
    meanderingOption : MeanderingAnalysisOption
         Compute or skip computation of dynamic wake meandering
    powerOption : PowerOption
         Compute or skip computation of power
    deficitOption : DeficitAnalysisOption
         Compute or read near field deficit
    focusOption : Focus
         Compute for a specific turbine or for the whole park
    angleChange : float
         Rotor angle change pr step(default 3.0)
    maxLaps : int
         Maximum number of rotor laps for profile convergence(default 30)
    deficitFileContents : DeficitFileContents
    deficitFileName : str
         (default None)
    ambientMixingParameter : float
         Ambient mixing parameters(default 0.0)
    deficitParameter : float
         Deficit parameter(default 0.0)
    multipleDeficitMethod : MultipleDeficitMethod
         Option for choosing the best approach for handling multiple deficits
    nearWakeLengthModel : NearWakeLengthModel
    viscosityFilter : ViscosityFilter
    incomingWind : IncomingWind
    speedIncrement : float
         Speed increment for calculation of deficits(default 0.25)
    deficitDepthFactor : float
         Factor on deficit depth(default 0.6)
    deficitGradientFactor : float
         Factor on depth derivative(default 0.35)
    cutOffFilterLengthFactor : float
         Cut off filter length in rotor diameter(default 2.0)
    windTurbineTypes : List[WindTurbineType]
    windParkLayout : List[WindParkTurbine]
    windVelocity : float
         Wind velocity (Constant wind)(default 0.0)
    windDirection : float
         Wind direction in global system (propagation direction)\n0 deg is along global X-direction\n90 deg is along global Y-direction(default 0.0)
    turbulenceIntencity : float
         Turbulence intencity ambient wind (fine mesh)(default 0.0)
    stabilityClass : StabilityClass
    coarseMeshFilename : str
         (default None)
    fineMeshFilename : str
         (default None)
    ambientWindFieldFilename : str
         (default None)
    turbulenceBoxOption : TurbulenceBoxOption
         Option for choosing whether turbulence boxes are made using DTU Mann (IECWind format) or TurbSim (Turbsim Bladed style format)
    outputPrefix : str
         Prefix in name of resulting wind files. File types are according to specified 'Turbulence Box Option'.  See the 'Wind specification' tab.(default 'diwa')
    includePowerResult : bool
         (default False)
    powerResultFormat : FileFormat
    includeVisualization : bool
         (default False)
    visualizationFormat : FileFormat
    animationTime : float
         (default 0.0)
    areaAveragingOption : AreaAveragingOption
         Option for selecting type of area averaging integration
    filterLengthOption : FilterLengthOption
         Option for selecting filter length type
    weightOption : WeightOption
         Weighting function option for calculating the meandering velocities
    weightConst : float
         (default 1.0)
    meanderingScaling : TurbulenceBoxScaling
    addedWakeScaling : TurbulenceBoxScaling
    ambientScaling : TurbulenceBoxScaling
    applyLowPassFilter : bool
         (default True)
    applyAreaAveraging : bool
         (default False)
    lowPassFrequencyOption : LowPassFrequencyOption
         Lowpass cutoff frequency option
    lowPassFrequency : float
         Cutoff frequency(default 0.0)
    useYawMisalignment : bool
         (default False)
    interpolateYawMisalignment : bool
         Option for interpolation on specified yaw misalignment performance relations(default False)
    wakeFlowModel : WakeFlowModel
    yawIncrement : float
         Yaw misalignment increment used in deficit computation(default 0.0)
    shaftDirectionDefinition : ShaftDirection
         Kind of shaft direction definition
    windTurbineMotions : List[WindTurbineMotion]
    useTimeWindow : bool
         If selected simulations will be performed for user defined start time and duration, otherwise DIWA will estimate the simulations time duration from turbulence boxes.(default False)
    timeWindowStart : float
         Starting time of meandering(default 0.0)
    timeWindowDuration : float
         Total duration of meandering(default 0.0)
    """

    def __init__(self , description="", airDensity=1.3, kinematicViscosity=1.824e-05, meanderingOption=MeanderingAnalysisOption.COMP, powerOption=PowerOption.COMP, deficitOption=DeficitAnalysisOption.COMP, focusOption=Focus.TARGET, angleChange=3.0, maxLaps=30, deficitFileContents=DeficitFileContents.INDUCTION_PROFILE, ambientMixingParameter=0.0, deficitParameter=0.0, multipleDeficitMethod=MultipleDeficitMethod.MAXOP, nearWakeLengthModel=NearWakeLengthModel.ROTOR_DIAMETERS, viscosityFilter=ViscosityFilter.MADSEN, incomingWind=IncomingWind.AMBIENT, speedIncrement=0.25, deficitDepthFactor=0.6, deficitGradientFactor=0.35, cutOffFilterLengthFactor=2.0, windVelocity=0.0, windDirection=0.0, turbulenceIntencity=0.0, stabilityClass=StabilityClass.NONE, turbulenceBoxOption=TurbulenceBoxOption.DTUMANN, outputPrefix='diwa', includePowerResult=False, powerResultFormat=FileFormat.BINARY, includeVisualization=False, visualizationFormat=FileFormat.BINARY, animationTime=0.0, areaAveragingOption=AreaAveragingOption.RADIAL, filterLengthOption=FilterLengthOption.ROTOR, weightOption=WeightOption.UNIFORM, weightConst=1.0, applyLowPassFilter=True, applyAreaAveraging=False, lowPassFrequencyOption=LowPassFrequencyOption.CALC, lowPassFrequency=0.0, useYawMisalignment=False, interpolateYawMisalignment=False, wakeFlowModel=WakeFlowModel.JIMENEZ, yawIncrement=0.0, shaftDirectionDefinition=ShaftDirection.YAW, useTimeWindow=False, timeWindowStart=0.0, timeWindowDuration=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.airDensity = airDensity
        self.kinematicViscosity = kinematicViscosity
        self.meanderingOption = meanderingOption
        self.powerOption = powerOption
        self.deficitOption = deficitOption
        self.focusOption = focusOption
        self.angleChange = angleChange
        self.maxLaps = maxLaps
        self.deficitFileContents = deficitFileContents
        self.deficitFileName = None
        self.ambientMixingParameter = ambientMixingParameter
        self.deficitParameter = deficitParameter
        self.multipleDeficitMethod = multipleDeficitMethod
        self.nearWakeLengthModel = nearWakeLengthModel
        self.viscosityFilter = viscosityFilter
        self.incomingWind = incomingWind
        self.speedIncrement = speedIncrement
        self.deficitDepthFactor = deficitDepthFactor
        self.deficitGradientFactor = deficitGradientFactor
        self.cutOffFilterLengthFactor = cutOffFilterLengthFactor
        self.windTurbineTypes = list()
        self.windParkLayout = list()
        self.windVelocity = windVelocity
        self.windDirection = windDirection
        self.turbulenceIntencity = turbulenceIntencity
        self.stabilityClass = stabilityClass
        self.coarseMeshFilename = None
        self.fineMeshFilename = None
        self.ambientWindFieldFilename = None
        self.turbulenceBoxOption = turbulenceBoxOption
        self.outputPrefix = outputPrefix
        self.includePowerResult = includePowerResult
        self.powerResultFormat = powerResultFormat
        self.includeVisualization = includeVisualization
        self.visualizationFormat = visualizationFormat
        self.animationTime = animationTime
        self.areaAveragingOption = areaAveragingOption
        self.filterLengthOption = filterLengthOption
        self.weightOption = weightOption
        self.weightConst = weightConst
        self.meanderingScaling = None
        self.addedWakeScaling = None
        self.ambientScaling = None
        self.applyLowPassFilter = applyLowPassFilter
        self.applyAreaAveraging = applyAreaAveraging
        self.lowPassFrequencyOption = lowPassFrequencyOption
        self.lowPassFrequency = lowPassFrequency
        self.useYawMisalignment = useYawMisalignment
        self.interpolateYawMisalignment = interpolateYawMisalignment
        self.wakeFlowModel = wakeFlowModel
        self.yawIncrement = yawIncrement
        self.shaftDirectionDefinition = shaftDirectionDefinition
        self.windTurbineMotions = list()
        self.useTimeWindow = useTimeWindow
        self.timeWindowStart = timeWindowStart
        self.timeWindowDuration = timeWindowDuration
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeneratorBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def airDensity(self) -> float:
        """"""
        return self.__airDensity

    @airDensity.setter
    def airDensity(self, value: float):
        """Set airDensity"""
        self.__airDensity = float(value)

    @property
    def kinematicViscosity(self) -> float:
        """"""
        return self.__kinematicViscosity

    @kinematicViscosity.setter
    def kinematicViscosity(self, value: float):
        """Set kinematicViscosity"""
        self.__kinematicViscosity = float(value)

    @property
    def meanderingOption(self) -> MeanderingAnalysisOption:
        """Compute or skip computation of dynamic wake meandering"""
        return self.__meanderingOption

    @meanderingOption.setter
    def meanderingOption(self, value: MeanderingAnalysisOption):
        """Set meanderingOption"""
        self.__meanderingOption = value

    @property
    def powerOption(self) -> PowerOption:
        """Compute or skip computation of power"""
        return self.__powerOption

    @powerOption.setter
    def powerOption(self, value: PowerOption):
        """Set powerOption"""
        self.__powerOption = value

    @property
    def deficitOption(self) -> DeficitAnalysisOption:
        """Compute or read near field deficit"""
        return self.__deficitOption

    @deficitOption.setter
    def deficitOption(self, value: DeficitAnalysisOption):
        """Set deficitOption"""
        self.__deficitOption = value

    @property
    def focusOption(self) -> Focus:
        """Compute for a specific turbine or for the whole park"""
        return self.__focusOption

    @focusOption.setter
    def focusOption(self, value: Focus):
        """Set focusOption"""
        self.__focusOption = value

    @property
    def angleChange(self) -> float:
        """Rotor angle change pr step"""
        return self.__angleChange

    @angleChange.setter
    def angleChange(self, value: float):
        """Set angleChange"""
        self.__angleChange = float(value)

    @property
    def maxLaps(self) -> int:
        """Maximum number of rotor laps for profile convergence"""
        return self.__maxLaps

    @maxLaps.setter
    def maxLaps(self, value: int):
        """Set maxLaps"""
        self.__maxLaps = int(value)

    @property
    def deficitFileContents(self) -> DeficitFileContents:
        """"""
        return self.__deficitFileContents

    @deficitFileContents.setter
    def deficitFileContents(self, value: DeficitFileContents):
        """Set deficitFileContents"""
        self.__deficitFileContents = value

    @property
    def deficitFileName(self) -> str:
        """"""
        return self.__deficitFileName

    @deficitFileName.setter
    def deficitFileName(self, value: str):
        """Set deficitFileName"""
        self.__deficitFileName = value

    @property
    def ambientMixingParameter(self) -> float:
        """Ambient mixing parameters"""
        return self.__ambientMixingParameter

    @ambientMixingParameter.setter
    def ambientMixingParameter(self, value: float):
        """Set ambientMixingParameter"""
        self.__ambientMixingParameter = float(value)

    @property
    def deficitParameter(self) -> float:
        """Deficit parameter"""
        return self.__deficitParameter

    @deficitParameter.setter
    def deficitParameter(self, value: float):
        """Set deficitParameter"""
        self.__deficitParameter = float(value)

    @property
    def multipleDeficitMethod(self) -> MultipleDeficitMethod:
        """Option for choosing the best approach for handling multiple deficits"""
        return self.__multipleDeficitMethod

    @multipleDeficitMethod.setter
    def multipleDeficitMethod(self, value: MultipleDeficitMethod):
        """Set multipleDeficitMethod"""
        self.__multipleDeficitMethod = value

    @property
    def nearWakeLengthModel(self) -> NearWakeLengthModel:
        """"""
        return self.__nearWakeLengthModel

    @nearWakeLengthModel.setter
    def nearWakeLengthModel(self, value: NearWakeLengthModel):
        """Set nearWakeLengthModel"""
        self.__nearWakeLengthModel = value

    @property
    def viscosityFilter(self) -> ViscosityFilter:
        """"""
        return self.__viscosityFilter

    @viscosityFilter.setter
    def viscosityFilter(self, value: ViscosityFilter):
        """Set viscosityFilter"""
        self.__viscosityFilter = value

    @property
    def incomingWind(self) -> IncomingWind:
        """"""
        return self.__incomingWind

    @incomingWind.setter
    def incomingWind(self, value: IncomingWind):
        """Set incomingWind"""
        self.__incomingWind = value

    @property
    def speedIncrement(self) -> float:
        """Speed increment for calculation of deficits"""
        return self.__speedIncrement

    @speedIncrement.setter
    def speedIncrement(self, value: float):
        """Set speedIncrement"""
        self.__speedIncrement = float(value)

    @property
    def deficitDepthFactor(self) -> float:
        """Factor on deficit depth"""
        return self.__deficitDepthFactor

    @deficitDepthFactor.setter
    def deficitDepthFactor(self, value: float):
        """Set deficitDepthFactor"""
        self.__deficitDepthFactor = float(value)

    @property
    def deficitGradientFactor(self) -> float:
        """Factor on depth derivative"""
        return self.__deficitGradientFactor

    @deficitGradientFactor.setter
    def deficitGradientFactor(self, value: float):
        """Set deficitGradientFactor"""
        self.__deficitGradientFactor = float(value)

    @property
    def cutOffFilterLengthFactor(self) -> float:
        """Cut off filter length in rotor diameter"""
        return self.__cutOffFilterLengthFactor

    @cutOffFilterLengthFactor.setter
    def cutOffFilterLengthFactor(self, value: float):
        """Set cutOffFilterLengthFactor"""
        self.__cutOffFilterLengthFactor = float(value)

    @property
    def windTurbineTypes(self) -> List[WindTurbineType]:
        """"""
        return self.__windTurbineTypes

    @windTurbineTypes.setter
    def windTurbineTypes(self, value: List[WindTurbineType]):
        """Set windTurbineTypes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__windTurbineTypes = value

    @property
    def windParkLayout(self) -> List[WindParkTurbine]:
        """"""
        return self.__windParkLayout

    @windParkLayout.setter
    def windParkLayout(self, value: List[WindParkTurbine]):
        """Set windParkLayout"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__windParkLayout = value

    @property
    def windVelocity(self) -> float:
        """Wind velocity (Constant wind)"""
        return self.__windVelocity

    @windVelocity.setter
    def windVelocity(self, value: float):
        """Set windVelocity"""
        self.__windVelocity = float(value)

    @property
    def windDirection(self) -> float:
        """Wind direction in global system (propagation direction)
0 deg is along global X-direction
90 deg is along global Y-direction"""
        return self.__windDirection

    @windDirection.setter
    def windDirection(self, value: float):
        """Set windDirection"""
        self.__windDirection = float(value)

    @property
    def turbulenceIntencity(self) -> float:
        """Turbulence intencity ambient wind (fine mesh)"""
        return self.__turbulenceIntencity

    @turbulenceIntencity.setter
    def turbulenceIntencity(self, value: float):
        """Set turbulenceIntencity"""
        self.__turbulenceIntencity = float(value)

    @property
    def stabilityClass(self) -> StabilityClass:
        """"""
        return self.__stabilityClass

    @stabilityClass.setter
    def stabilityClass(self, value: StabilityClass):
        """Set stabilityClass"""
        self.__stabilityClass = value

    @property
    def coarseMeshFilename(self) -> str:
        """"""
        return self.__coarseMeshFilename

    @coarseMeshFilename.setter
    def coarseMeshFilename(self, value: str):
        """Set coarseMeshFilename"""
        self.__coarseMeshFilename = value

    @property
    def fineMeshFilename(self) -> str:
        """"""
        return self.__fineMeshFilename

    @fineMeshFilename.setter
    def fineMeshFilename(self, value: str):
        """Set fineMeshFilename"""
        self.__fineMeshFilename = value

    @property
    def ambientWindFieldFilename(self) -> str:
        """"""
        return self.__ambientWindFieldFilename

    @ambientWindFieldFilename.setter
    def ambientWindFieldFilename(self, value: str):
        """Set ambientWindFieldFilename"""
        self.__ambientWindFieldFilename = value

    @property
    def turbulenceBoxOption(self) -> TurbulenceBoxOption:
        """Option for choosing whether turbulence boxes are made using DTU Mann (IECWind format) or TurbSim (Turbsim Bladed style format)"""
        return self.__turbulenceBoxOption

    @turbulenceBoxOption.setter
    def turbulenceBoxOption(self, value: TurbulenceBoxOption):
        """Set turbulenceBoxOption"""
        self.__turbulenceBoxOption = value

    @property
    def outputPrefix(self) -> str:
        """Prefix in name of resulting wind files. File types are according to specified 'Turbulence Box Option'.  See the 'Wind specification' tab."""
        return self.__outputPrefix

    @outputPrefix.setter
    def outputPrefix(self, value: str):
        """Set outputPrefix"""
        self.__outputPrefix = value

    @property
    def includePowerResult(self) -> bool:
        """"""
        return self.__includePowerResult

    @includePowerResult.setter
    def includePowerResult(self, value: bool):
        """Set includePowerResult"""
        self.__includePowerResult = bool(value)

    @property
    def powerResultFormat(self) -> FileFormat:
        """"""
        return self.__powerResultFormat

    @powerResultFormat.setter
    def powerResultFormat(self, value: FileFormat):
        """Set powerResultFormat"""
        self.__powerResultFormat = value

    @property
    def includeVisualization(self) -> bool:
        """"""
        return self.__includeVisualization

    @includeVisualization.setter
    def includeVisualization(self, value: bool):
        """Set includeVisualization"""
        self.__includeVisualization = bool(value)

    @property
    def visualizationFormat(self) -> FileFormat:
        """"""
        return self.__visualizationFormat

    @visualizationFormat.setter
    def visualizationFormat(self, value: FileFormat):
        """Set visualizationFormat"""
        self.__visualizationFormat = value

    @property
    def animationTime(self) -> float:
        """"""
        return self.__animationTime

    @animationTime.setter
    def animationTime(self, value: float):
        """Set animationTime"""
        self.__animationTime = float(value)

    @property
    def areaAveragingOption(self) -> AreaAveragingOption:
        """Option for selecting type of area averaging integration"""
        return self.__areaAveragingOption

    @areaAveragingOption.setter
    def areaAveragingOption(self, value: AreaAveragingOption):
        """Set areaAveragingOption"""
        self.__areaAveragingOption = value

    @property
    def filterLengthOption(self) -> FilterLengthOption:
        """Option for selecting filter length type"""
        return self.__filterLengthOption

    @filterLengthOption.setter
    def filterLengthOption(self, value: FilterLengthOption):
        """Set filterLengthOption"""
        self.__filterLengthOption = value

    @property
    def weightOption(self) -> WeightOption:
        """Weighting function option for calculating the meandering velocities"""
        return self.__weightOption

    @weightOption.setter
    def weightOption(self, value: WeightOption):
        """Set weightOption"""
        self.__weightOption = value

    @property
    def weightConst(self) -> float:
        """"""
        return self.__weightConst

    @weightConst.setter
    def weightConst(self, value: float):
        """Set weightConst"""
        self.__weightConst = float(value)

    @property
    def meanderingScaling(self) -> TurbulenceBoxScaling:
        """"""
        return self.__meanderingScaling

    @meanderingScaling.setter
    def meanderingScaling(self, value: TurbulenceBoxScaling):
        """Set meanderingScaling"""
        self.__meanderingScaling = value

    @property
    def addedWakeScaling(self) -> TurbulenceBoxScaling:
        """"""
        return self.__addedWakeScaling

    @addedWakeScaling.setter
    def addedWakeScaling(self, value: TurbulenceBoxScaling):
        """Set addedWakeScaling"""
        self.__addedWakeScaling = value

    @property
    def ambientScaling(self) -> TurbulenceBoxScaling:
        """"""
        return self.__ambientScaling

    @ambientScaling.setter
    def ambientScaling(self, value: TurbulenceBoxScaling):
        """Set ambientScaling"""
        self.__ambientScaling = value

    @property
    def applyLowPassFilter(self) -> bool:
        """"""
        return self.__applyLowPassFilter

    @applyLowPassFilter.setter
    def applyLowPassFilter(self, value: bool):
        """Set applyLowPassFilter"""
        self.__applyLowPassFilter = bool(value)

    @property
    def applyAreaAveraging(self) -> bool:
        """"""
        return self.__applyAreaAveraging

    @applyAreaAveraging.setter
    def applyAreaAveraging(self, value: bool):
        """Set applyAreaAveraging"""
        self.__applyAreaAveraging = bool(value)

    @property
    def lowPassFrequencyOption(self) -> LowPassFrequencyOption:
        """Lowpass cutoff frequency option"""
        return self.__lowPassFrequencyOption

    @lowPassFrequencyOption.setter
    def lowPassFrequencyOption(self, value: LowPassFrequencyOption):
        """Set lowPassFrequencyOption"""
        self.__lowPassFrequencyOption = value

    @property
    def lowPassFrequency(self) -> float:
        """Cutoff frequency"""
        return self.__lowPassFrequency

    @lowPassFrequency.setter
    def lowPassFrequency(self, value: float):
        """Set lowPassFrequency"""
        self.__lowPassFrequency = float(value)

    @property
    def useYawMisalignment(self) -> bool:
        """"""
        return self.__useYawMisalignment

    @useYawMisalignment.setter
    def useYawMisalignment(self, value: bool):
        """Set useYawMisalignment"""
        self.__useYawMisalignment = bool(value)

    @property
    def interpolateYawMisalignment(self) -> bool:
        """Option for interpolation on specified yaw misalignment performance relations"""
        return self.__interpolateYawMisalignment

    @interpolateYawMisalignment.setter
    def interpolateYawMisalignment(self, value: bool):
        """Set interpolateYawMisalignment"""
        self.__interpolateYawMisalignment = bool(value)

    @property
    def wakeFlowModel(self) -> WakeFlowModel:
        """"""
        return self.__wakeFlowModel

    @wakeFlowModel.setter
    def wakeFlowModel(self, value: WakeFlowModel):
        """Set wakeFlowModel"""
        self.__wakeFlowModel = value

    @property
    def yawIncrement(self) -> float:
        """Yaw misalignment increment used in deficit computation"""
        return self.__yawIncrement

    @yawIncrement.setter
    def yawIncrement(self, value: float):
        """Set yawIncrement"""
        self.__yawIncrement = float(value)

    @property
    def shaftDirectionDefinition(self) -> ShaftDirection:
        """Kind of shaft direction definition"""
        return self.__shaftDirectionDefinition

    @shaftDirectionDefinition.setter
    def shaftDirectionDefinition(self, value: ShaftDirection):
        """Set shaftDirectionDefinition"""
        self.__shaftDirectionDefinition = value

    @property
    def windTurbineMotions(self) -> List[WindTurbineMotion]:
        """"""
        return self.__windTurbineMotions

    @windTurbineMotions.setter
    def windTurbineMotions(self, value: List[WindTurbineMotion]):
        """Set windTurbineMotions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__windTurbineMotions = value

    @property
    def useTimeWindow(self) -> bool:
        """If selected simulations will be performed for user defined start time and duration, otherwise DIWA will estimate the simulations time duration from turbulence boxes."""
        return self.__useTimeWindow

    @useTimeWindow.setter
    def useTimeWindow(self, value: bool):
        """Set useTimeWindow"""
        self.__useTimeWindow = bool(value)

    @property
    def timeWindowStart(self) -> float:
        """Starting time of meandering"""
        return self.__timeWindowStart

    @timeWindowStart.setter
    def timeWindowStart(self, value: float):
        """Set timeWindowStart"""
        self.__timeWindowStart = float(value)

    @property
    def timeWindowDuration(self) -> float:
        """Total duration of meandering"""
        return self.__timeWindowDuration

    @timeWindowDuration.setter
    def timeWindowDuration(self, value: float):
        """Set timeWindowDuration"""
        self.__timeWindowDuration = float(value)

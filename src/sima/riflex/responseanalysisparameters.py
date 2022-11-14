# This an autogenerated file
# 
# Generated with ResponseAnalysisParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.responseanalysisparameters import ResponseAnalysisParametersBlueprint
from typing import Dict
from sima.riflex.additionalstructuraldampingparameters import AdditionalStructuralDampingParameters
from sima.riflex.convergencecriterion import ConvergenceCriterion
from sima.riflex.forceswitch import ForceSwitch
from sima.riflex.printswitch import PrintSwitch
from sima.riflex.responsefrequencyoption import ResponseFrequencyOption
from sima.riflex.responseiterationmethod import ResponseIterationMethod
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ResponseAnalysisParameters(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    iterationMethod : ResponseIterationMethod
         Response iteration method
    retry : bool
         If the response iteration does not converge a second attempt will be made with the other response iteration method(default False)
    maxNumberOfIterations : int
         Maximum number of iterations(default 30)
    convergenceCriterion : ConvergenceCriterion
         Convergence criterion
    convergenceLimit : float
         Convergence limit for the iteration(default 0.0001)
    initialResponseEstimate : float
         Scaling factor for the initial response estimate(default 0.5)
    responseFrequencyOption : ResponseFrequencyOption
         Option for combining response frequencies
    numberOfDominatingFrequencies : int
         Number of dominating frequencies given in user defined frequency\nranking(default 0)
    amplitudeLimit : float
         Amplitude limit for including frequency normalized by\nthe minimum diameter.(default 0.01)
    lowerFrequencyCutoff : float
         Cut-off excitation parameter ration for frequencies below the identified dominating frequency.(default 0.0)
    upperFrequencyCutoff : float
         Cut-off excitation parameter ration for frequencies above the identified dominating frequency.(default 0.0)
    relativeStructuralDamping : float
         Relative structural damping(default 0.0)
    forceSwitch : ForceSwitch
         Option for force calculation
    printSwitch : PrintSwitch
         Print switch
    additionalStructuralDampingSpecification : bool
         This data group allows additional material and slip damping to be specified for some or all segments in the system. \nThis structural damping is read from separate files and is applied in addition to the relative structural damping level RELDAM. \nThe structural damping is given as a function of the response curvature and is therefore updated during the response iterations.(default False)
    additionalStructuralDampingParameters : List[AdditionalStructuralDampingParameters]
    """

    def __init__(self , description="", _id=None, iterationMethod=ResponseIterationMethod.NEWTON_RAPHSON, retry=False, maxNumberOfIterations=30, convergenceCriterion=ConvergenceCriterion.AMPNOR, convergenceLimit=0.0001, initialResponseEstimate=0.5, responseFrequencyOption=ResponseFrequencyOption.CONCURRENT, numberOfDominatingFrequencies=0, amplitudeLimit=0.01, lowerFrequencyCutoff=0.0, upperFrequencyCutoff=0.0, relativeStructuralDamping=0.0, forceSwitch=ForceSwitch.USE_CURVATURE, printSwitch=PrintSwitch.FINAL_RESULTS, additionalStructuralDampingSpecification=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.iterationMethod = iterationMethod
        self.retry = retry
        self.maxNumberOfIterations = maxNumberOfIterations
        self.convergenceCriterion = convergenceCriterion
        self.convergenceLimit = convergenceLimit
        self.initialResponseEstimate = initialResponseEstimate
        self.responseFrequencyOption = responseFrequencyOption
        self.numberOfDominatingFrequencies = numberOfDominatingFrequencies
        self.amplitudeLimit = amplitudeLimit
        self.lowerFrequencyCutoff = lowerFrequencyCutoff
        self.upperFrequencyCutoff = upperFrequencyCutoff
        self.relativeStructuralDamping = relativeStructuralDamping
        self.forceSwitch = forceSwitch
        self.printSwitch = printSwitch
        self.additionalStructuralDampingSpecification = additionalStructuralDampingSpecification
        self.additionalStructuralDampingParameters = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ResponseAnalysisParametersBlueprint()


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
    def iterationMethod(self) -> ResponseIterationMethod:
        """Response iteration method"""
        return self.__iterationMethod

    @iterationMethod.setter
    def iterationMethod(self, value: ResponseIterationMethod):
        """Set iterationMethod"""
        self.__iterationMethod = value

    @property
    def retry(self) -> bool:
        """If the response iteration does not converge a second attempt will be made with the other response iteration method"""
        return self.__retry

    @retry.setter
    def retry(self, value: bool):
        """Set retry"""
        self.__retry = bool(value)

    @property
    def maxNumberOfIterations(self) -> int:
        """Maximum number of iterations"""
        return self.__maxNumberOfIterations

    @maxNumberOfIterations.setter
    def maxNumberOfIterations(self, value: int):
        """Set maxNumberOfIterations"""
        self.__maxNumberOfIterations = int(value)

    @property
    def convergenceCriterion(self) -> ConvergenceCriterion:
        """Convergence criterion"""
        return self.__convergenceCriterion

    @convergenceCriterion.setter
    def convergenceCriterion(self, value: ConvergenceCriterion):
        """Set convergenceCriterion"""
        self.__convergenceCriterion = value

    @property
    def convergenceLimit(self) -> float:
        """Convergence limit for the iteration"""
        return self.__convergenceLimit

    @convergenceLimit.setter
    def convergenceLimit(self, value: float):
        """Set convergenceLimit"""
        self.__convergenceLimit = float(value)

    @property
    def initialResponseEstimate(self) -> float:
        """Scaling factor for the initial response estimate"""
        return self.__initialResponseEstimate

    @initialResponseEstimate.setter
    def initialResponseEstimate(self, value: float):
        """Set initialResponseEstimate"""
        self.__initialResponseEstimate = float(value)

    @property
    def responseFrequencyOption(self) -> ResponseFrequencyOption:
        """Option for combining response frequencies"""
        return self.__responseFrequencyOption

    @responseFrequencyOption.setter
    def responseFrequencyOption(self, value: ResponseFrequencyOption):
        """Set responseFrequencyOption"""
        self.__responseFrequencyOption = value

    @property
    def numberOfDominatingFrequencies(self) -> int:
        """Number of dominating frequencies given in user defined frequency
ranking"""
        return self.__numberOfDominatingFrequencies

    @numberOfDominatingFrequencies.setter
    def numberOfDominatingFrequencies(self, value: int):
        """Set numberOfDominatingFrequencies"""
        self.__numberOfDominatingFrequencies = int(value)

    @property
    def amplitudeLimit(self) -> float:
        """Amplitude limit for including frequency normalized by
the minimum diameter."""
        return self.__amplitudeLimit

    @amplitudeLimit.setter
    def amplitudeLimit(self, value: float):
        """Set amplitudeLimit"""
        self.__amplitudeLimit = float(value)

    @property
    def lowerFrequencyCutoff(self) -> float:
        """Cut-off excitation parameter ration for frequencies below the identified dominating frequency."""
        return self.__lowerFrequencyCutoff

    @lowerFrequencyCutoff.setter
    def lowerFrequencyCutoff(self, value: float):
        """Set lowerFrequencyCutoff"""
        self.__lowerFrequencyCutoff = float(value)

    @property
    def upperFrequencyCutoff(self) -> float:
        """Cut-off excitation parameter ration for frequencies above the identified dominating frequency."""
        return self.__upperFrequencyCutoff

    @upperFrequencyCutoff.setter
    def upperFrequencyCutoff(self, value: float):
        """Set upperFrequencyCutoff"""
        self.__upperFrequencyCutoff = float(value)

    @property
    def relativeStructuralDamping(self) -> float:
        """Relative structural damping"""
        return self.__relativeStructuralDamping

    @relativeStructuralDamping.setter
    def relativeStructuralDamping(self, value: float):
        """Set relativeStructuralDamping"""
        self.__relativeStructuralDamping = float(value)

    @property
    def forceSwitch(self) -> ForceSwitch:
        """Option for force calculation"""
        return self.__forceSwitch

    @forceSwitch.setter
    def forceSwitch(self, value: ForceSwitch):
        """Set forceSwitch"""
        self.__forceSwitch = value

    @property
    def printSwitch(self) -> PrintSwitch:
        """Print switch"""
        return self.__printSwitch

    @printSwitch.setter
    def printSwitch(self, value: PrintSwitch):
        """Set printSwitch"""
        self.__printSwitch = value

    @property
    def additionalStructuralDampingSpecification(self) -> bool:
        """This data group allows additional material and slip damping to be specified for some or all segments in the system. 
This structural damping is read from separate files and is applied in addition to the relative structural damping level RELDAM. 
The structural damping is given as a function of the response curvature and is therefore updated during the response iterations."""
        return self.__additionalStructuralDampingSpecification

    @additionalStructuralDampingSpecification.setter
    def additionalStructuralDampingSpecification(self, value: bool):
        """Set additionalStructuralDampingSpecification"""
        self.__additionalStructuralDampingSpecification = bool(value)

    @property
    def additionalStructuralDampingParameters(self) -> List[AdditionalStructuralDampingParameters]:
        """"""
        return self.__additionalStructuralDampingParameters

    @additionalStructuralDampingParameters.setter
    def additionalStructuralDampingParameters(self, value: List[AdditionalStructuralDampingParameters]):
        """Set additionalStructuralDampingParameters"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__additionalStructuralDampingParameters = value

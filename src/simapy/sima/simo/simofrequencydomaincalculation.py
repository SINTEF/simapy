# This an autogenerated file
# 
# Generated with SIMOFrequencyDomainCalculation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simofrequencydomaincalculation import SIMOFrequencyDomainCalculationBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .frequencyanalysistype import FrequencyAnalysisType
from .frequencydomainbodyitem import FrequencyDomainBodyItem
from .frequencyrangedefinition import FrequencyRangeDefinition
from .frequnecydomainlineitem import FrequnecyDomainLineItem
from .linearization import Linearization

class SIMOFrequencyDomainCalculation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    analysisType : FrequencyAnalysisType
    linearization : Linearization
    maximumNumberOfIterations : int
         (default 10)
    bodies : List[FrequencyDomainBodyItem]
    frequencyRangeLF : FrequencyRangeDefinition
    frequencyRangeWF : FrequencyRangeDefinition
    calculateLineDynamics : bool
         (default False)
    estimationTime : float
         (default 10800.0)
    specifyLinesToSimulate : bool
         (default False)
    linesToSimulate : List[FrequnecyDomainLineItem]
    """

    def __init__(self , description="", analysisType=FrequencyAnalysisType.WAVE_FREQUENCY, linearization=Linearization.STOCHASTIC, maximumNumberOfIterations=10, calculateLineDynamics=False, estimationTime=10800.0, specifyLinesToSimulate=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.analysisType = analysisType
        self.linearization = linearization
        self.maximumNumberOfIterations = maximumNumberOfIterations
        self.bodies = list()
        self.frequencyRangeLF = None
        self.frequencyRangeWF = None
        self.calculateLineDynamics = calculateLineDynamics
        self.estimationTime = estimationTime
        self.specifyLinesToSimulate = specifyLinesToSimulate
        self.linesToSimulate = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMOFrequencyDomainCalculationBlueprint()


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
    def analysisType(self) -> FrequencyAnalysisType:
        """"""
        return self.__analysisType

    @analysisType.setter
    def analysisType(self, value: FrequencyAnalysisType):
        """Set analysisType"""
        self.__analysisType = value

    @property
    def linearization(self) -> Linearization:
        """"""
        return self.__linearization

    @linearization.setter
    def linearization(self, value: Linearization):
        """Set linearization"""
        self.__linearization = value

    @property
    def maximumNumberOfIterations(self) -> int:
        """"""
        return self.__maximumNumberOfIterations

    @maximumNumberOfIterations.setter
    def maximumNumberOfIterations(self, value: int):
        """Set maximumNumberOfIterations"""
        self.__maximumNumberOfIterations = int(value)

    @property
    def bodies(self) -> List[FrequencyDomainBodyItem]:
        """"""
        return self.__bodies

    @bodies.setter
    def bodies(self, value: List[FrequencyDomainBodyItem]):
        """Set bodies"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__bodies = value

    @property
    def frequencyRangeLF(self) -> FrequencyRangeDefinition:
        """"""
        return self.__frequencyRangeLF

    @frequencyRangeLF.setter
    def frequencyRangeLF(self, value: FrequencyRangeDefinition):
        """Set frequencyRangeLF"""
        self.__frequencyRangeLF = value

    @property
    def frequencyRangeWF(self) -> FrequencyRangeDefinition:
        """"""
        return self.__frequencyRangeWF

    @frequencyRangeWF.setter
    def frequencyRangeWF(self, value: FrequencyRangeDefinition):
        """Set frequencyRangeWF"""
        self.__frequencyRangeWF = value

    @property
    def calculateLineDynamics(self) -> bool:
        """"""
        return self.__calculateLineDynamics

    @calculateLineDynamics.setter
    def calculateLineDynamics(self, value: bool):
        """Set calculateLineDynamics"""
        self.__calculateLineDynamics = bool(value)

    @property
    def estimationTime(self) -> float:
        """"""
        return self.__estimationTime

    @estimationTime.setter
    def estimationTime(self, value: float):
        """Set estimationTime"""
        self.__estimationTime = float(value)

    @property
    def specifyLinesToSimulate(self) -> bool:
        """"""
        return self.__specifyLinesToSimulate

    @specifyLinesToSimulate.setter
    def specifyLinesToSimulate(self, value: bool):
        """Set specifyLinesToSimulate"""
        self.__specifyLinesToSimulate = bool(value)

    @property
    def linesToSimulate(self) -> List[FrequnecyDomainLineItem]:
        """"""
        return self.__linesToSimulate

    @linesToSimulate.setter
    def linesToSimulate(self, value: List[FrequnecyDomainLineItem]):
        """Set linesToSimulate"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__linesToSimulate = value

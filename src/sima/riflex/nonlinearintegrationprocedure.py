# This an autogenerated file
# 
# Generated with NonLinearIntegrationProcedure
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.nonlinearintegrationprocedure import NonLinearIntegrationProcedureBlueprint
from typing import Dict
from .convergencenorm import ConvergenceNorm
from .iterationcontinuationcode import IterationContinuationCode
from .iterationtype import IterationType
from sima.sima import MOAO
from sima.sima import ScriptableValue

class NonLinearIntegrationProcedure(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    equilibriumIterationFrequency : int
         Frequency of equilibrium iteration(default 1)
    iterationType : IterationType
         Type of iteration if iteration is to be performed
    maxIterations : int
         Maximum number of iterations for steps with iteration(default 10)
    convergenceNorm : ConvergenceNorm
    equilibriumIterationAccuracy : float
         Desired accuracy for equilibrium iteration measured by a modified euclidian displacement norm (norm of squared translations). Recommended values: 10e-6 - 10e-5.(default 1e-05)
    energyAccuracy : float
         Required accuracy measured by energy norm. This value is relevant only if Convergence Norm is 'Both'.(default 1e-05)
    iterationContinuation : IterationContinuationCode
         Code for continuation after iteration
    autoTimeStepSubdivision : int
         Code for automatic subdivision of time step(default 0)
    timeIntegrationInfo : int
         Code for time integration information(default 1)
    """

    def __init__(self , description="", equilibriumIterationFrequency=1, iterationType=IterationType.TRUE_NEWTON_RAPHSON, maxIterations=10, convergenceNorm=ConvergenceNorm.DISP, equilibriumIterationAccuracy=1e-05, energyAccuracy=1e-05, iterationContinuation=IterationContinuationCode.CONTINUED, autoTimeStepSubdivision=0, timeIntegrationInfo=1, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.equilibriumIterationFrequency = equilibriumIterationFrequency
        self.iterationType = iterationType
        self.maxIterations = maxIterations
        self.convergenceNorm = convergenceNorm
        self.equilibriumIterationAccuracy = equilibriumIterationAccuracy
        self.energyAccuracy = energyAccuracy
        self.iterationContinuation = iterationContinuation
        self.autoTimeStepSubdivision = autoTimeStepSubdivision
        self.timeIntegrationInfo = timeIntegrationInfo
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NonLinearIntegrationProcedureBlueprint()


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
    def equilibriumIterationFrequency(self) -> int:
        """Frequency of equilibrium iteration"""
        return self.__equilibriumIterationFrequency

    @equilibriumIterationFrequency.setter
    def equilibriumIterationFrequency(self, value: int):
        """Set equilibriumIterationFrequency"""
        self.__equilibriumIterationFrequency = int(value)

    @property
    def iterationType(self) -> IterationType:
        """Type of iteration if iteration is to be performed"""
        return self.__iterationType

    @iterationType.setter
    def iterationType(self, value: IterationType):
        """Set iterationType"""
        self.__iterationType = value

    @property
    def maxIterations(self) -> int:
        """Maximum number of iterations for steps with iteration"""
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, value: int):
        """Set maxIterations"""
        self.__maxIterations = int(value)

    @property
    def convergenceNorm(self) -> ConvergenceNorm:
        """"""
        return self.__convergenceNorm

    @convergenceNorm.setter
    def convergenceNorm(self, value: ConvergenceNorm):
        """Set convergenceNorm"""
        self.__convergenceNorm = value

    @property
    def equilibriumIterationAccuracy(self) -> float:
        """Desired accuracy for equilibrium iteration measured by a modified euclidian displacement norm (norm of squared translations). Recommended values: 10e-6 - 10e-5."""
        return self.__equilibriumIterationAccuracy

    @equilibriumIterationAccuracy.setter
    def equilibriumIterationAccuracy(self, value: float):
        """Set equilibriumIterationAccuracy"""
        self.__equilibriumIterationAccuracy = float(value)

    @property
    def energyAccuracy(self) -> float:
        """Required accuracy measured by energy norm. This value is relevant only if Convergence Norm is 'Both'."""
        return self.__energyAccuracy

    @energyAccuracy.setter
    def energyAccuracy(self, value: float):
        """Set energyAccuracy"""
        self.__energyAccuracy = float(value)

    @property
    def iterationContinuation(self) -> IterationContinuationCode:
        """Code for continuation after iteration"""
        return self.__iterationContinuation

    @iterationContinuation.setter
    def iterationContinuation(self, value: IterationContinuationCode):
        """Set iterationContinuation"""
        self.__iterationContinuation = value

    @property
    def autoTimeStepSubdivision(self) -> int:
        """Code for automatic subdivision of time step"""
        return self.__autoTimeStepSubdivision

    @autoTimeStepSubdivision.setter
    def autoTimeStepSubdivision(self, value: int):
        """Set autoTimeStepSubdivision"""
        self.__autoTimeStepSubdivision = int(value)

    @property
    def timeIntegrationInfo(self) -> int:
        """Code for time integration information"""
        return self.__timeIntegrationInfo

    @timeIntegrationInfo.setter
    def timeIntegrationInfo(self, value: int):
        """Set timeIntegrationInfo"""
        self.__timeIntegrationInfo = int(value)

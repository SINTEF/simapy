# This an autogenerated file
# 
# Generated with OptimizationCalculationParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.optimizationcalculationparameters import OptimizationCalculationParametersBlueprint
from typing import Dict
from sima.sima import MOAO
from sima.sima import ScriptableValue

class OptimizationCalculationParameters(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    desiredFinalAccuracy : float
         Desired final accuracy. Should not be much smaller than the accuracy by which the gradients are computed.(default 0.01)
    tolerance : float
         Tolerance needed for the QP solver to perform several tests, for example whether optimality conditions are satisfied or whether a  number is considered as zero or not.(default 1e-12)
    minStepLength : float
         Minimum step length in case there is more than one parallel system. Recommended is any value in the order of the accuracy by which the functions are computed.(default 1e-12)
    maxFunctionCalls : int
         Maximum number of function calls during line search. Should not be larger than 50.(default 20)
    maxIterations : int
         Maximum number of outer iterations, where one iteration corresponds to one formulation and solution of the quadratic programming subproblem, or, alternatively one evaluation of the gradients.(default 20)
    stackSize : int
         Stack size for storing merit function values at previous iterations for non-monotone line search. If set to zero, monotone line search is performed. Should not be greater than 50.(default 10)
    automaticNormalization : bool
         Automatic normalization of optimization problem(default True)
    handleFailure : bool
         Try another solution if the underlying calculation fails(default True)
    """

    def __init__(self , description="", desiredFinalAccuracy=0.01, tolerance=1e-12, minStepLength=1e-12, maxFunctionCalls=20, maxIterations=20, stackSize=10, automaticNormalization=True, handleFailure=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.desiredFinalAccuracy = desiredFinalAccuracy
        self.tolerance = tolerance
        self.minStepLength = minStepLength
        self.maxFunctionCalls = maxFunctionCalls
        self.maxIterations = maxIterations
        self.stackSize = stackSize
        self.automaticNormalization = automaticNormalization
        self.handleFailure = handleFailure
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OptimizationCalculationParametersBlueprint()


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
    def desiredFinalAccuracy(self) -> float:
        """Desired final accuracy. Should not be much smaller than the accuracy by which the gradients are computed."""
        return self.__desiredFinalAccuracy

    @desiredFinalAccuracy.setter
    def desiredFinalAccuracy(self, value: float):
        """Set desiredFinalAccuracy"""
        self.__desiredFinalAccuracy = float(value)

    @property
    def tolerance(self) -> float:
        """Tolerance needed for the QP solver to perform several tests, for example whether optimality conditions are satisfied or whether a  number is considered as zero or not."""
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        """Set tolerance"""
        self.__tolerance = float(value)

    @property
    def minStepLength(self) -> float:
        """Minimum step length in case there is more than one parallel system. Recommended is any value in the order of the accuracy by which the functions are computed."""
        return self.__minStepLength

    @minStepLength.setter
    def minStepLength(self, value: float):
        """Set minStepLength"""
        self.__minStepLength = float(value)

    @property
    def maxFunctionCalls(self) -> int:
        """Maximum number of function calls during line search. Should not be larger than 50."""
        return self.__maxFunctionCalls

    @maxFunctionCalls.setter
    def maxFunctionCalls(self, value: int):
        """Set maxFunctionCalls"""
        self.__maxFunctionCalls = int(value)

    @property
    def maxIterations(self) -> int:
        """Maximum number of outer iterations, where one iteration corresponds to one formulation and solution of the quadratic programming subproblem, or, alternatively one evaluation of the gradients."""
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, value: int):
        """Set maxIterations"""
        self.__maxIterations = int(value)

    @property
    def stackSize(self) -> int:
        """Stack size for storing merit function values at previous iterations for non-monotone line search. If set to zero, monotone line search is performed. Should not be greater than 50."""
        return self.__stackSize

    @stackSize.setter
    def stackSize(self, value: int):
        """Set stackSize"""
        self.__stackSize = int(value)

    @property
    def automaticNormalization(self) -> bool:
        """Automatic normalization of optimization problem"""
        return self.__automaticNormalization

    @automaticNormalization.setter
    def automaticNormalization(self, value: bool):
        """Set automaticNormalization"""
        self.__automaticNormalization = bool(value)

    @property
    def handleFailure(self) -> bool:
        """Try another solution if the underlying calculation fails"""
        return self.__handleFailure

    @handleFailure.setter
    def handleFailure(self, value: bool):
        """Set handleFailure"""
        self.__handleFailure = bool(value)

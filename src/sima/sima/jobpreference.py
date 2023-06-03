# This an autogenerated file
# 
# Generated with JobPreference
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.jobpreference import JobPreferenceBlueprint
from typing import Dict
from .scriptablevalue import ScriptableValue
from .simapreference import SIMAPreference

class JobPreference(SIMAPreference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    computeConditionsAutomatically : bool
         Compute concurrent condition runs automatically(default True)
    maxConditionRuns : int
         Maximum number of concurrent condition runs(default 0)
    computeWorkflowsAutomatically : bool
         Compute concurrent condition runs automatically(default True)
    maxWorkflowRuns : int
         Maximum number of concurrent workflow runs(default 0)
    """

    def __init__(self , description="", computeConditionsAutomatically=True, maxConditionRuns=0, computeWorkflowsAutomatically=True, maxWorkflowRuns=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.computeConditionsAutomatically = computeConditionsAutomatically
        self.maxConditionRuns = maxConditionRuns
        self.computeWorkflowsAutomatically = computeWorkflowsAutomatically
        self.maxWorkflowRuns = maxWorkflowRuns
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return JobPreferenceBlueprint()


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
    def computeConditionsAutomatically(self) -> bool:
        """Compute concurrent condition runs automatically"""
        return self.__computeConditionsAutomatically

    @computeConditionsAutomatically.setter
    def computeConditionsAutomatically(self, value: bool):
        """Set computeConditionsAutomatically"""
        self.__computeConditionsAutomatically = bool(value)

    @property
    def maxConditionRuns(self) -> int:
        """Maximum number of concurrent condition runs"""
        return self.__maxConditionRuns

    @maxConditionRuns.setter
    def maxConditionRuns(self, value: int):
        """Set maxConditionRuns"""
        self.__maxConditionRuns = int(value)

    @property
    def computeWorkflowsAutomatically(self) -> bool:
        """Compute concurrent condition runs automatically"""
        return self.__computeWorkflowsAutomatically

    @computeWorkflowsAutomatically.setter
    def computeWorkflowsAutomatically(self, value: bool):
        """Set computeWorkflowsAutomatically"""
        self.__computeWorkflowsAutomatically = bool(value)

    @property
    def maxWorkflowRuns(self) -> int:
        """Maximum number of concurrent workflow runs"""
        return self.__maxWorkflowRuns

    @maxWorkflowRuns.setter
    def maxWorkflowRuns(self, value: int):
        """Set maxWorkflowRuns"""
        self.__maxWorkflowRuns = int(value)

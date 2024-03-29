# This an autogenerated file
# 
# Generated with WamitResultContainer
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wamitresultcontainer import WamitResultContainerBlueprint
from typing import Dict
from ..sima import ConditionResultContainer
from ..sima import Property
from ..sima import ScriptableValue
from .wamitresultentry import WamitResultEntry

class WamitResultContainer(ConditionResultContainer):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[Property]
    modelOutputFile : str
         (default None)
    probability : float
         (default 0.0)
    calculationResults : WamitResultEntry
    potenResult : WamitResultEntry
    """

    def __init__(self , description="", probability=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.modelOutputFile = None
        self.probability = probability
        self.calculationResults = None
        self.potenResult = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WamitResultContainerBlueprint()


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
    def properties(self) -> List[Property]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[Property]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def modelOutputFile(self) -> str:
        """"""
        return self.__modelOutputFile

    @modelOutputFile.setter
    def modelOutputFile(self, value: str):
        """Set modelOutputFile"""
        self.__modelOutputFile = value

    @property
    def probability(self) -> float:
        """"""
        return self.__probability

    @probability.setter
    def probability(self, value: float):
        """Set probability"""
        self.__probability = float(value)

    @property
    def calculationResults(self) -> WamitResultEntry:
        """"""
        return self.__calculationResults

    @calculationResults.setter
    def calculationResults(self, value: WamitResultEntry):
        """Set calculationResults"""
        self.__calculationResults = value

    @property
    def potenResult(self) -> WamitResultEntry:
        """"""
        return self.__potenResult

    @potenResult.setter
    def potenResult(self, value: WamitResultEntry):
        """Set potenResult"""
        self.__potenResult = value

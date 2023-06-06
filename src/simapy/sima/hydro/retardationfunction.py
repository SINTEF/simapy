# This an autogenerated file
# 
# Generated with RetardationFunction
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.retardationfunction import RetardationFunctionBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .lineardampingmatrix import LinearDampingMatrix
from .retardationelementdata import RetardationElementData

class RetardationFunction(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    retardationElements : List[RetardationElementData]
    timeDelay : float
         (default 0.0)
    additionalDamping : LinearDampingMatrix
    """

    def __init__(self , description="", timeDelay=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.retardationElements = list()
        self.timeDelay = timeDelay
        self.additionalDamping = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RetardationFunctionBlueprint()


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
    def retardationElements(self) -> List[RetardationElementData]:
        """"""
        return self.__retardationElements

    @retardationElements.setter
    def retardationElements(self, value: List[RetardationElementData]):
        """Set retardationElements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__retardationElements = value

    @property
    def timeDelay(self) -> float:
        """"""
        return self.__timeDelay

    @timeDelay.setter
    def timeDelay(self, value: float):
        """Set timeDelay"""
        self.__timeDelay = float(value)

    @property
    def additionalDamping(self) -> LinearDampingMatrix:
        """"""
        return self.__additionalDamping

    @additionalDamping.setter
    def additionalDamping(self, value: LinearDampingMatrix):
        """Set additionalDamping"""
        self.__additionalDamping = value

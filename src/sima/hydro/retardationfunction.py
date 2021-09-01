# This an autogenerated file
# 
# Generated with RetardationFunction
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.retardationfunction import RetardationFunctionBlueprint
from sima.hydro.lineardampingmatrix import LinearDampingMatrix
from sima.hydro.retardationelementdata import RetardationElementData
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class RetardationFunction(MOAO):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    retardationElements : List[RetardationElementData]
    timeDelay : float
         (default 0.0)
    additionalDamping : LinearDampingMatrix
    """

    def __init__(self , name:str="", description:str="", _id:str="", timeDelay:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__retardationElements = list()
        self.__timeDelay = timeDelay
        self.__additionalDamping = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RetardationFunctionBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def retardationElements(self) -> List[RetardationElementData]:
        """"""
        return self.__retardationElements

    @retardationElements.setter
    def retardationElements(self, value: List[RetardationElementData]):
        """Set retardationElements"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
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

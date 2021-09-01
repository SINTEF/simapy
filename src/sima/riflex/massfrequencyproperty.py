# This an autogenerated file
# 
# Generated with MassFrequencyProperty
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.massfrequencyproperty import MassFrequencyPropertyBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class MassFrequencyProperty(MOAO):
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
    nonDimensionalFrequency : float
         Non-dimensional frequency(default 0.0)
    addedMassCoefficient : float
         Added mass coefficient(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", nonDimensionalFrequency:float=0.0, addedMassCoefficient:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__nonDimensionalFrequency = nonDimensionalFrequency
        self.__addedMassCoefficient = addedMassCoefficient
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MassFrequencyPropertyBlueprint()


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
    def nonDimensionalFrequency(self) -> float:
        """Non-dimensional frequency"""
        return self.__nonDimensionalFrequency

    @nonDimensionalFrequency.setter
    def nonDimensionalFrequency(self, value: float):
        """Set nonDimensionalFrequency"""
        self.__nonDimensionalFrequency = float(value)

    @property
    def addedMassCoefficient(self) -> float:
        """Added mass coefficient"""
        return self.__addedMassCoefficient

    @addedMassCoefficient.setter
    def addedMassCoefficient(self, value: float):
        """Set addedMassCoefficient"""
        self.__addedMassCoefficient = float(value)

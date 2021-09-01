# This an autogenerated file
# 
# Generated with ComplexValues
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.complexvalues import ComplexValuesBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ComplexValues(MOAO):
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
    realValues : Sequence[float]
    imagValues : Sequence[float]
    """

    def __init__(self , name:str="", description:str="", _id:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__realValues = list()
        self.__imagValues = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ComplexValuesBlueprint()


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
    def realValues(self) -> Sequence[float]:
        """"""
        return self.__realValues

    @realValues.setter
    def realValues(self, value: Sequence[float]):
        """Set realValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__realValues = value

    @property
    def imagValues(self) -> Sequence[float]:
        """"""
        return self.__imagValues

    @imagValues.setter
    def imagValues(self, value: Sequence[float]):
        """Set imagValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__imagValues = value

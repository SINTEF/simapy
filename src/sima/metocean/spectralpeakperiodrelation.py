# This an autogenerated file
# 
# Generated with SpectralPeakPeriodRelation
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.spectralpeakperiodrelation import SpectralPeakPeriodRelationBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class SpectralPeakPeriodRelation(MOAO):
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
    hs : Sequence[float]
    interval5 : Sequence[float]
    mean : Sequence[float]
    interval95 : Sequence[float]
    """

    def __init__(self , name:str="", description:str="", _id:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__hs = list()
        self.__interval5 = list()
        self.__mean = list()
        self.__interval95 = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SpectralPeakPeriodRelationBlueprint()


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
    def hs(self) -> Sequence[float]:
        """"""
        return self.__hs

    @hs.setter
    def hs(self, value: Sequence[float]):
        """Set hs"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__hs = value

    @property
    def interval5(self) -> Sequence[float]:
        """"""
        return self.__interval5

    @interval5.setter
    def interval5(self, value: Sequence[float]):
        """Set interval5"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__interval5 = value

    @property
    def mean(self) -> Sequence[float]:
        """"""
        return self.__mean

    @mean.setter
    def mean(self, value: Sequence[float]):
        """Set mean"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__mean = value

    @property
    def interval95(self) -> Sequence[float]:
        """"""
        return self.__interval95

    @interval95.setter
    def interval95(self, value: Sequence[float]):
        """Set interval95"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__interval95 = value

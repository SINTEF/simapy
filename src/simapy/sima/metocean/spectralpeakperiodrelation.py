# This an autogenerated file
# 
# Generated with SpectralPeakPeriodRelation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.spectralpeakperiodrelation import SpectralPeakPeriodRelationBlueprint
from numpy import ndarray,asarray
from ..sima import MOAO
from ..sima import ScriptableValue

class SpectralPeakPeriodRelation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    hs : ndarray of float
    interval5 : ndarray of float
    mean : ndarray of float
    interval95 : ndarray of float
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.hs = []
        self.interval5 = []
        self.mean = []
        self.interval95 = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SpectralPeakPeriodRelationBlueprint()


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
    def hs(self) -> ndarray:
        """"""
        return self.__hs

    @hs.setter
    def hs(self, value: ndarray):
        """Set hs"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__hs = array

    @property
    def interval5(self) -> ndarray:
        """"""
        return self.__interval5

    @interval5.setter
    def interval5(self, value: ndarray):
        """Set interval5"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__interval5 = array

    @property
    def mean(self) -> ndarray:
        """"""
        return self.__mean

    @mean.setter
    def mean(self, value: ndarray):
        """Set mean"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__mean = array

    @property
    def interval95(self) -> ndarray:
        """"""
        return self.__interval95

    @interval95.setter
    def interval95(self, value: ndarray):
        """Set interval95"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__interval95 = array
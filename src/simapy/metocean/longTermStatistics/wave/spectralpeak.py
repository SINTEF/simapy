# This an autogenerated file
# Spectral peak for Tp as a function of Hs.
# Generated with SpectralPeak
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.spectralpeak import SpectralPeakBlueprint
from numpy import ndarray,asarray
from dmt.entity import Entity

class SpectralPeak(Entity):
    """
    Spectral peak for Tp as a function of Hs.
    Keyword arguments
    -----------------
    description : str
         (default "")
    Hs : ndarray
         Hs.
    int5 : ndarray
         5%-interval
    mean : ndarray
         mean.
    int95 : ndarray
         95 %-interval
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.Hs = []
        self.int5 = []
        self.mean = []
        self.int95 = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SpectralPeakBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def Hs(self) -> ndarray:
        """Hs."""
        return self.__Hs

    @Hs.setter
    def Hs(self, value: ndarray):
        """Set Hs"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__Hs = array

    @property
    def int5(self) -> ndarray:
        """5%-interval"""
        return self.__int5

    @int5.setter
    def int5(self, value: ndarray):
        """Set int5"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__int5 = array

    @property
    def mean(self) -> ndarray:
        """mean."""
        return self.__mean

    @mean.setter
    def mean(self, value: ndarray):
        """Set mean"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__mean = array

    @property
    def int95(self) -> ndarray:
        """95 %-interval"""
        return self.__int95

    @int95.setter
    def int95(self, value: ndarray):
        """Set int95"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__int95 = array

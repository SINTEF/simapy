# This an autogenerated file
# CONTOUR LINES OF HS-TP.
# Generated with Contour
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.contour import ContourBlueprint
from numpy import ndarray,asarray
from dmt.entity import Entity

class Contour(Entity):
    """
    CONTOUR LINES OF HS-TP.
    Keyword arguments
    -----------------
    description : str
         (default "")
    Hs : ndarray
         Hs.
    Tp : ndarray
         Tp
    returnPeriod : float
         return period(default 0.0)
    """

    def __init__(self , description="", returnPeriod=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.Hs = []
        self.Tp = []
        self.returnPeriod = returnPeriod
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ContourBlueprint()


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
    def Tp(self) -> ndarray:
        """Tp"""
        return self.__Tp

    @Tp.setter
    def Tp(self, value: ndarray):
        """Set Tp"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__Tp = array

    @property
    def returnPeriod(self) -> float:
        """return period"""
        return self.__returnPeriod

    @returnPeriod.setter
    def returnPeriod(self, value: float):
        """Set returnPeriod"""
        self.__returnPeriod = float(value)

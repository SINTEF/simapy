# This an autogenerated file
# EXTREME VALUES FOR DIFFERENT PROBABILITY.
# Generated with ExtremeValues
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.extremevalues import ExtremeValuesBlueprint
from numpy import ndarray,asarray
from dmt.entity import Entity

class ExtremeValues(Entity):
    """
    EXTREME VALUES FOR DIFFERENT PROBABILITY.
    Keyword arguments
    -----------------
    description : str
         (default "")
    variable : str
         variable.(default None)
    returnPeriods : ndarray
         return periods
    extremes : ndarray
         extreme values for the variable
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.variable = None
        self.returnPeriods = []
        self.extremes = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExtremeValuesBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def variable(self) -> str:
        """variable."""
        return self.__variable

    @variable.setter
    def variable(self, value: str):
        """Set variable"""
        self.__variable = value

    @property
    def returnPeriods(self) -> ndarray:
        """return periods"""
        return self.__returnPeriods

    @returnPeriods.setter
    def returnPeriods(self, value: ndarray):
        """Set returnPeriods"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__returnPeriods = array

    @property
    def extremes(self) -> ndarray:
        """extreme values for the variable"""
        return self.__extremes

    @extremes.setter
    def extremes(self, value: ndarray):
        """Set extremes"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__extremes = array

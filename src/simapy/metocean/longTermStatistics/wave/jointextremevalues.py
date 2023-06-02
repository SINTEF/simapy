# This an autogenerated file
# JOINED EXTREME VALUES FOR DIFFERENT PROBABILITY.
# Generated with JointExtremeValues
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.jointextremevalues import JointExtremeValuesBlueprint
from numpy import ndarray,asarray
from dmt.entity import Entity

class JointExtremeValues(Entity):
    """
    JOINED EXTREME VALUES FOR DIFFERENT PROBABILITY.
    Keyword arguments
    -----------------
    description : str
         (default "")
    var1 : str
         first variable.(default None)
    var2 : str
         second variable.(default None)
    returnPeriods : ndarray
         return periods
    var1Extremes : ndarray
         extreme values for the variable 1
    var2Extremes : ndarray
         extreme values for the variable 2
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.var1 = None
        self.var2 = None
        self.returnPeriods = []
        self.var1Extremes = []
        self.var2Extremes = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return JointExtremeValuesBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def var1(self) -> str:
        """first variable."""
        return self.__var1

    @var1.setter
    def var1(self, value: str):
        """Set var1"""
        self.__var1 = value

    @property
    def var2(self) -> str:
        """second variable."""
        return self.__var2

    @var2.setter
    def var2(self, value: str):
        """Set var2"""
        self.__var2 = value

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
    def var1Extremes(self) -> ndarray:
        """extreme values for the variable 1"""
        return self.__var1Extremes

    @var1Extremes.setter
    def var1Extremes(self, value: ndarray):
        """Set var1Extremes"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__var1Extremes = array

    @property
    def var2Extremes(self) -> ndarray:
        """extreme values for the variable 2"""
        return self.__var2Extremes

    @var2Extremes.setter
    def var2Extremes(self, value: ndarray):
        """Set var2Extremes"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__var2Extremes = array

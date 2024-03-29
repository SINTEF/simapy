# This an autogenerated file
# 
# Generated with DiffractedWaveElevation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.diffractedwaveelevation import DiffractedWaveElevationBlueprint
from numpy import ndarray,asarray
from ..sima import MOAO
from ..sima import ScriptableValue
from .directiondependentcomplexvalues import DirectionDependentComplexValues

class DiffractedWaveElevation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    directions : ndarray of float
    frequencies : ndarray of float
    elevation : DirectionDependentComplexValues
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.directions = []
        self.frequencies = []
        self.elevation = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DiffractedWaveElevationBlueprint()


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
    def directions(self) -> ndarray:
        """"""
        return self.__directions

    @directions.setter
    def directions(self, value: ndarray):
        """Set directions"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__directions = array

    @property
    def frequencies(self) -> ndarray:
        """"""
        return self.__frequencies

    @frequencies.setter
    def frequencies(self, value: ndarray):
        """Set frequencies"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__frequencies = array

    @property
    def elevation(self) -> DirectionDependentComplexValues:
        """"""
        return self.__elevation

    @elevation.setter
    def elevation(self, value: DirectionDependentComplexValues):
        """Set elevation"""
        self.__elevation = value

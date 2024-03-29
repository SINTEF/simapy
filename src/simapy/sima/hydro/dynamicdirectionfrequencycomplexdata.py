# This an autogenerated file
# 
# Generated with DynamicDirectionFrequencyComplexData
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamicdirectionfrequencycomplexdata import DynamicDirectionFrequencyComplexDataBlueprint
from numpy import ndarray,asarray
from ..sima import MOAO
from ..sima import ScriptableValue
from .directiondependentcomplexvalues import DirectionDependentComplexValues

class DynamicDirectionFrequencyComplexData(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    directions : ndarray of float
    frequencies : ndarray of float
    dofs : List[DirectionDependentComplexValues]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.directions = []
        self.frequencies = []
        self.dofs = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicDirectionFrequencyComplexDataBlueprint()


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
    def dofs(self) -> List[DirectionDependentComplexValues]:
        """"""
        return self.__dofs

    @dofs.setter
    def dofs(self, value: List[DirectionDependentComplexValues]):
        """Set dofs"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__dofs = value

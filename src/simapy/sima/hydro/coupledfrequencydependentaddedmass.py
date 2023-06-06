# This an autogenerated file
# 
# Generated with CoupledFrequencyDependentAddedMass
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.coupledfrequencydependentaddedmass import CoupledFrequencyDependentAddedMassBlueprint
from numpy import ndarray,asarray
from ..sima import MOAO
from ..sima import ScriptableValue
from .twodofdata import TwoDofData

class CoupledFrequencyDependentAddedMass(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    frequencies : ndarray of float
    items : List[TwoDofData]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.frequencies = []
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CoupledFrequencyDependentAddedMassBlueprint()


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
    def items(self) -> List[TwoDofData]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[TwoDofData]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__items = value

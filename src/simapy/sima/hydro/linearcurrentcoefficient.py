# This an autogenerated file
# 
# Generated with LinearCurrentCoefficient
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.linearcurrentcoefficient import LinearCurrentCoefficientBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .directionsymmetry import DirectionSymmetry
from .linearcurrentcoefficientitem import LinearCurrentCoefficientItem

class LinearCurrentCoefficient(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    symmetry : DirectionSymmetry
    items : List[LinearCurrentCoefficientItem]
    """

    def __init__(self , description="", symmetry=DirectionSymmetry.NO_SYMMETRY, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.symmetry = symmetry
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LinearCurrentCoefficientBlueprint()


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
    def symmetry(self) -> DirectionSymmetry:
        """"""
        return self.__symmetry

    @symmetry.setter
    def symmetry(self, value: DirectionSymmetry):
        """Set symmetry"""
        self.__symmetry = value

    @property
    def items(self) -> List[LinearCurrentCoefficientItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[LinearCurrentCoefficientItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__items = value

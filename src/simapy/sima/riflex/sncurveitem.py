# This an autogenerated file
# 
# Generated with SNCurveItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.sncurveitem import SNCurveItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class SNCurveItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    slope : float
         Slope of curve segment(default 0.0)
    transitionPoint : float
         Transition point between curve segment (i-1) and i - logN(default 0.0)
    """

    def __init__(self , description="", slope=0.0, transitionPoint=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.slope = slope
        self.transitionPoint = transitionPoint
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SNCurveItemBlueprint()


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
    def slope(self) -> float:
        """Slope of curve segment"""
        return self.__slope

    @slope.setter
    def slope(self, value: float):
        """Set slope"""
        self.__slope = float(value)

    @property
    def transitionPoint(self) -> float:
        """Transition point between curve segment (i-1) and i - logN"""
        return self.__transitionPoint

    @transitionPoint.setter
    def transitionPoint(self, value: float):
        """Set transitionPoint"""
        self.__transitionPoint = float(value)

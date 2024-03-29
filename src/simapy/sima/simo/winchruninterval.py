# This an autogenerated file
# 
# Generated with WinchRunInterval
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.winchruninterval import WinchRunIntervalBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class WinchRunInterval(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    startTime : float
         Start time for running winch(default 0.0)
    stopTime : float
         Stop time for running winch(default 0.0)
    speed : float
         Winch run velocity (positive when paying out)(default 0.0)
    """

    def __init__(self , description="", startTime=0.0, stopTime=0.0, speed=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.startTime = startTime
        self.stopTime = stopTime
        self.speed = speed
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WinchRunIntervalBlueprint()


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
    def startTime(self) -> float:
        """Start time for running winch"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def stopTime(self) -> float:
        """Stop time for running winch"""
        return self.__stopTime

    @stopTime.setter
    def stopTime(self, value: float):
        """Set stopTime"""
        self.__stopTime = float(value)

    @property
    def speed(self) -> float:
        """Winch run velocity (positive when paying out)"""
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        """Set speed"""
        self.__speed = float(value)

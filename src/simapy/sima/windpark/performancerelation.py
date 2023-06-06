# This an autogenerated file
# 
# Generated with PerformanceRelation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.performancerelation import PerformanceRelationBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class PerformanceRelation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    windSpeed : float
         (default 0.0)
    rotorSpeed : float
         (default 0.0)
    bladePitch : float
         (default 0.0)
    power : float
         (default 0.0)
    thrust : float
         (default 0.0)
    """

    def __init__(self , description="", windSpeed=0.0, rotorSpeed=0.0, bladePitch=0.0, power=0.0, thrust=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.windSpeed = windSpeed
        self.rotorSpeed = rotorSpeed
        self.bladePitch = bladePitch
        self.power = power
        self.thrust = thrust
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PerformanceRelationBlueprint()


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
    def windSpeed(self) -> float:
        """"""
        return self.__windSpeed

    @windSpeed.setter
    def windSpeed(self, value: float):
        """Set windSpeed"""
        self.__windSpeed = float(value)

    @property
    def rotorSpeed(self) -> float:
        """"""
        return self.__rotorSpeed

    @rotorSpeed.setter
    def rotorSpeed(self, value: float):
        """Set rotorSpeed"""
        self.__rotorSpeed = float(value)

    @property
    def bladePitch(self) -> float:
        """"""
        return self.__bladePitch

    @bladePitch.setter
    def bladePitch(self, value: float):
        """Set bladePitch"""
        self.__bladePitch = float(value)

    @property
    def power(self) -> float:
        """"""
        return self.__power

    @power.setter
    def power(self, value: float):
        """Set power"""
        self.__power = float(value)

    @property
    def thrust(self) -> float:
        """"""
        return self.__thrust

    @thrust.setter
    def thrust(self, value: float):
        """Set thrust"""
        self.__thrust = float(value)

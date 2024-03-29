# This an autogenerated file
# 
# Generated with MotionSequence
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.motionsequence import MotionSequenceBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class MotionSequence(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    start : float
         Sequence start time(default 0.0)
    stop : float
         Sequence stop time(default 0.0)
    deltaPos : float
         Change in position during sequence(default 0.0)
    speed : float
         Sequence travelling speed after ramp-up(default 0.0)
    acceleration : float
         Acceleration / retardation for start and stop of sequence(default 0.0)
    """

    def __init__(self , description="", start=0.0, stop=0.0, deltaPos=0.0, speed=0.0, acceleration=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.start = start
        self.stop = stop
        self.deltaPos = deltaPos
        self.speed = speed
        self.acceleration = acceleration
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MotionSequenceBlueprint()


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
    def start(self) -> float:
        """Sequence start time"""
        return self.__start

    @start.setter
    def start(self, value: float):
        """Set start"""
        self.__start = float(value)

    @property
    def stop(self) -> float:
        """Sequence stop time"""
        return self.__stop

    @stop.setter
    def stop(self, value: float):
        """Set stop"""
        self.__stop = float(value)

    @property
    def deltaPos(self) -> float:
        """Change in position during sequence"""
        return self.__deltaPos

    @deltaPos.setter
    def deltaPos(self, value: float):
        """Set deltaPos"""
        self.__deltaPos = float(value)

    @property
    def speed(self) -> float:
        """Sequence travelling speed after ramp-up"""
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        """Set speed"""
        self.__speed = float(value)

    @property
    def acceleration(self) -> float:
        """Acceleration / retardation for start and stop of sequence"""
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, value: float):
        """Set acceleration"""
        self.__acceleration = float(value)

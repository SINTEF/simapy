# This an autogenerated file
# Description for stochastic process at a sector.
# Generated with WindCurrent
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.windcurrent import WindCurrentBlueprint
from numpy import ndarray,asarray
from dmt.entity import Entity

class WindCurrent(Entity):
    """
    Description for stochastic process at a sector.
    Keyword arguments
    -----------------
    description : str
         (default "")
    level : float
         measured level.(default 0.0)
    direction : ndarray
         the scatter data for direction.
    speed : ndarray
         the scatter data for speed.
    """

    def __init__(self , description="", level=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.level = level
        self.direction = []
        self.speed = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WindCurrentBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def level(self) -> float:
        """measured level."""
        return self.__level

    @level.setter
    def level(self, value: float):
        """Set level"""
        self.__level = float(value)

    @property
    def direction(self) -> ndarray:
        """the scatter data for direction."""
        return self.__direction

    @direction.setter
    def direction(self, value: ndarray):
        """Set direction"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 2:
            raise ValueError("Expected array with 2 dimensions")
        self.__direction = array

    @property
    def speed(self) -> ndarray:
        """the scatter data for speed."""
        return self.__speed

    @speed.setter
    def speed(self, value: ndarray):
        """Set speed"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 2:
            raise ValueError("Expected array with 2 dimensions")
        self.__speed = array

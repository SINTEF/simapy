# This an autogenerated file
# Description for stochastic wind.
# Generated with StochasticWind
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stochasticwind import StochasticWindBlueprint
from numpy import ndarray,asarray
from dmt.namedentity import NamedEntity

class StochasticWind(NamedEntity):
    """
    Description for stochastic wind.
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         name for the metocean data.(default None)
    speed : ndarray
         mean wind speed.
    direction : ndarray
         wind direction.
    level : float
         at this level, upward positive.(default 0.0)
    """

    def __init__(self , description="", level=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = None
        self.speed = []
        self.direction = []
        self.level = level
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StochasticWindBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def name(self) -> str:
        """name for the metocean data."""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def speed(self) -> ndarray:
        """mean wind speed."""
        return self.__speed

    @speed.setter
    def speed(self, value: ndarray):
        """Set speed"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__speed = array

    @property
    def direction(self) -> ndarray:
        """wind direction."""
        return self.__direction

    @direction.setter
    def direction(self, value: ndarray):
        """Set direction"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__direction = array

    @property
    def level(self) -> float:
        """at this level, upward positive."""
        return self.__level

    @level.setter
    def level(self, value: float):
        """Set level"""
        self.__level = float(value)

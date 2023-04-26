# This an autogenerated file
# Description for hindcast metocean data.
# Generated with Hindcast
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hindcast import HindcastBlueprint
from numpy import ndarray,asarray
from .stochasticcurrent import StochasticCurrent
from .stochasticwave import StochasticWave
from .stochasticwind import StochasticWind
from dmt.namedentity import NamedEntity

class Hindcast(NamedEntity):
    """
    Description for hindcast metocean data.
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         name for the metocean data.(default None)
    date : ndarray
         date string.
    wave : List[StochasticWave]
         wave models.
    wind : List[StochasticWind]
         wind models.
    current : List[StochasticCurrent]
         current models.
    latitude : float
         (default 0.0)
    longitude : float
         (default 0.0)
    """

    def __init__(self , description="", latitude=0.0, longitude=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = None
        self.date = []
        self.wave = list()
        self.wind = list()
        self.current = list()
        self.latitude = latitude
        self.longitude = longitude
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HindcastBlueprint()


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
    def date(self) -> ndarray:
        """date string."""
        return self.__date

    @date.setter
    def date(self, value: ndarray):
        """Set date"""
        array = asarray(value, dtype=str)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__date = array

    @property
    def wave(self) -> List[StochasticWave]:
        """wave models."""
        return self.__wave

    @wave.setter
    def wave(self, value: List[StochasticWave]):
        """Set wave"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__wave = value

    @property
    def wind(self) -> List[StochasticWind]:
        """wind models."""
        return self.__wind

    @wind.setter
    def wind(self, value: List[StochasticWind]):
        """Set wind"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__wind = value

    @property
    def current(self) -> List[StochasticCurrent]:
        """current models."""
        return self.__current

    @current.setter
    def current(self, value: List[StochasticCurrent]):
        """Set current"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__current = value

    @property
    def latitude(self) -> float:
        """"""
        return self.__latitude

    @latitude.setter
    def latitude(self, value: float):
        """Set latitude"""
        self.__latitude = float(value)

    @property
    def longitude(self) -> float:
        """"""
        return self.__longitude

    @longitude.setter
    def longitude(self, value: float):
        """Set longitude"""
        self.__longitude = float(value)
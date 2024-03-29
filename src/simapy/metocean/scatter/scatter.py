# This an autogenerated file
# Description for scatter data based on Hs-Tp.
# Generated with Scatter
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scatter import ScatterBlueprint
from numpy import ndarray,asarray
from .sector import Sector
from dmt.namedentity import NamedEntity

class Scatter(NamedEntity):
    """
    Description for scatter data based on Hs-Tp.
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         name for the scatter data as appear in SIMA.(default None)
    hsUpperLimits : ndarray
         upper limits of the boundaries for each row in the scatter data.
    tpUpperLimits : ndarray
         upper limits of the boundaries for each column in the scatter data.
    seaStateDuration : float
         duration of sea state.(default 0.0)
    countingPeriod : float
         the duration which is used to count the occurrence of events.(default 0.0)
    sectors : List[Sector]
         sector scatter data.
    omni : Sector
         omni scatter data.
    """

    def __init__(self , description="", seaStateDuration=0.0, countingPeriod=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = None
        self.hsUpperLimits = []
        self.tpUpperLimits = []
        self.seaStateDuration = seaStateDuration
        self.countingPeriod = countingPeriod
        self.sectors = list()
        self.omni = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScatterBlueprint()


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
        """name for the scatter data as appear in SIMA."""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def hsUpperLimits(self) -> ndarray:
        """upper limits of the boundaries for each row in the scatter data."""
        return self.__hsUpperLimits

    @hsUpperLimits.setter
    def hsUpperLimits(self, value: ndarray):
        """Set hsUpperLimits"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__hsUpperLimits = array

    @property
    def tpUpperLimits(self) -> ndarray:
        """upper limits of the boundaries for each column in the scatter data."""
        return self.__tpUpperLimits

    @tpUpperLimits.setter
    def tpUpperLimits(self, value: ndarray):
        """Set tpUpperLimits"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__tpUpperLimits = array

    @property
    def seaStateDuration(self) -> float:
        """duration of sea state."""
        return self.__seaStateDuration

    @seaStateDuration.setter
    def seaStateDuration(self, value: float):
        """Set seaStateDuration"""
        self.__seaStateDuration = float(value)

    @property
    def countingPeriod(self) -> float:
        """the duration which is used to count the occurrence of events."""
        return self.__countingPeriod

    @countingPeriod.setter
    def countingPeriod(self, value: float):
        """Set countingPeriod"""
        self.__countingPeriod = float(value)

    @property
    def sectors(self) -> List[Sector]:
        """sector scatter data."""
        return self.__sectors

    @sectors.setter
    def sectors(self, value: List[Sector]):
        """Set sectors"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__sectors = value

    @property
    def omni(self) -> Sector:
        """omni scatter data."""
        return self.__omni

    @omni.setter
    def omni(self, value: Sector):
        """Set omni"""
        self.__omni = value

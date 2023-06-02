# This an autogenerated file
# Description for stochastic process with sampling.
# Generated with Profile
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.profile import ProfileBlueprint
from typing import Dict
from ..hsbinnedsector import HsBinnedSector
from ..sector import Sector
from dmt.namedentity import NamedEntity

class Profile(NamedEntity):
    """
    Description for stochastic process with sampling.
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         name for statistics at this level, e.g. level10m.(default None)
    level : float
         sampling rate in hours.(default 0.0)
    sectors : List[Sector]
         sectoral representation of wind/current at this sampling rate.
    omni : Sector
         omni representation of wind/current at this sampling rate.
    sectoralHsBinned : List[HsBinnedSector]
         sectoral representation of wind/current binned for different Hs at this sampling rate.
    omniHsBinned : HsBinnedSector
         omni representation of wind/current binned for different Hs at this sampling rate.
    """

    def __init__(self , description="", level=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = None
        self.level = level
        self.sectors = list()
        self.omni = None
        self.sectoralHsBinned = list()
        self.omniHsBinned = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ProfileBlueprint()


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
        """name for statistics at this level, e.g. level10m."""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def level(self) -> float:
        """sampling rate in hours."""
        return self.__level

    @level.setter
    def level(self, value: float):
        """Set level"""
        self.__level = float(value)

    @property
    def sectors(self) -> List[Sector]:
        """sectoral representation of wind/current at this sampling rate."""
        return self.__sectors

    @sectors.setter
    def sectors(self, value: List[Sector]):
        """Set sectors"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__sectors = value

    @property
    def omni(self) -> Sector:
        """omni representation of wind/current at this sampling rate."""
        return self.__omni

    @omni.setter
    def omni(self, value: Sector):
        """Set omni"""
        self.__omni = value

    @property
    def sectoralHsBinned(self) -> List[HsBinnedSector]:
        """sectoral representation of wind/current binned for different Hs at this sampling rate."""
        return self.__sectoralHsBinned

    @sectoralHsBinned.setter
    def sectoralHsBinned(self, value: List[HsBinnedSector]):
        """Set sectoralHsBinned"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__sectoralHsBinned = value

    @property
    def omniHsBinned(self) -> HsBinnedSector:
        """omni representation of wind/current binned for different Hs at this sampling rate."""
        return self.__omniHsBinned

    @omniHsBinned.setter
    def omniHsBinned(self, value: HsBinnedSector):
        """Set omniHsBinned"""
        self.__omniHsBinned = value

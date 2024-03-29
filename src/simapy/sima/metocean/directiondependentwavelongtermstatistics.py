# This an autogenerated file
# 
# Generated with DirectionDependentWaveLongTermStatistics
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.directiondependentwavelongtermstatistics import DirectionDependentWaveLongTermStatisticsBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .wavelongtermstatistics import WaveLongTermStatistics
from .wavesector import WaveSector

class DirectionDependentWaveLongTermStatistics(WaveLongTermStatistics):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    sectors : List[WaveSector]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.sectors = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DirectionDependentWaveLongTermStatisticsBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def sectors(self) -> List[WaveSector]:
        """"""
        return self.__sectors

    @sectors.setter
    def sectors(self, value: List[WaveSector]):
        """Set sectors"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__sectors = value

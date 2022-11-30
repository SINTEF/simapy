# This an autogenerated file
# 
# Generated with LongTermStatisticsWaveCalculation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.longtermstatisticswavecalculation import LongTermStatisticsWaveCalculationBlueprint
from typing import Dict
from sima.metocean.calculationdirection import CalculationDirection
from sima.metocean.wavestatisticsmethod import WaveStatisticsMethod
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.metocean.wavelongtermstatistics import WaveLongTermStatistics
    from sima.metocean.omnidirectionalwavelongtermstatistics import OmniDirectionalWaveLongTermStatistics

class LongTermStatisticsWaveCalculation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    returnPeriod : float
         (default 0.0)
    statistics : WaveLongTermStatistics
    omni : OmniDirectionalWaveLongTermStatistics
    method : WaveStatisticsMethod
    directions : List[CalculationDirection]
    """

    def __init__(self , description="", returnPeriod=0.0, method=WaveStatisticsMethod.FROM_DISTRIBUTION, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.returnPeriod = returnPeriod
        self.statistics = None
        self.omni = None
        self.method = method
        self.directions = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LongTermStatisticsWaveCalculationBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def returnPeriod(self) -> float:
        """"""
        return self.__returnPeriod

    @returnPeriod.setter
    def returnPeriod(self, value: float):
        """Set returnPeriod"""
        self.__returnPeriod = float(value)

    @property
    def statistics(self) -> WaveLongTermStatistics:
        """"""
        return self.__statistics

    @statistics.setter
    def statistics(self, value: WaveLongTermStatistics):
        """Set statistics"""
        self.__statistics = value

    @property
    def omni(self) -> OmniDirectionalWaveLongTermStatistics:
        """"""
        return self.__omni

    @omni.setter
    def omni(self, value: OmniDirectionalWaveLongTermStatistics):
        """Set omni"""
        self.__omni = value

    @property
    def method(self) -> WaveStatisticsMethod:
        """"""
        return self.__method

    @method.setter
    def method(self, value: WaveStatisticsMethod):
        """Set method"""
        self.__method = value

    @property
    def directions(self) -> List[CalculationDirection]:
        """"""
        return self.__directions

    @directions.setter
    def directions(self, value: List[CalculationDirection]):
        """Set directions"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__directions = value

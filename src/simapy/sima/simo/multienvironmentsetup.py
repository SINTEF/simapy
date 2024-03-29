# This an autogenerated file
# 
# Generated with MultiEnvironmentSetup
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.multienvironmentsetup import MultiEnvironmentSetupBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class MultiEnvironmentSetup(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    windWaveLowerFrequency : float
         Wind wave lower frequency limit(default 0.1)
    windWaveUpperFrequency : float
         Wind wave upper frequency limit(default 3.0)
    swellWaveLowerFrequency : float
         Swell wave lower frequency limit(default 0.05)
    swellWaveUpperFrequency : float
         Swell wave upper frequency limit(default 2.0)
    """

    def __init__(self , description="", windWaveLowerFrequency=0.1, windWaveUpperFrequency=3.0, swellWaveLowerFrequency=0.05, swellWaveUpperFrequency=2.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.windWaveLowerFrequency = windWaveLowerFrequency
        self.windWaveUpperFrequency = windWaveUpperFrequency
        self.swellWaveLowerFrequency = swellWaveLowerFrequency
        self.swellWaveUpperFrequency = swellWaveUpperFrequency
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MultiEnvironmentSetupBlueprint()


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
    def windWaveLowerFrequency(self) -> float:
        """Wind wave lower frequency limit"""
        return self.__windWaveLowerFrequency

    @windWaveLowerFrequency.setter
    def windWaveLowerFrequency(self, value: float):
        """Set windWaveLowerFrequency"""
        self.__windWaveLowerFrequency = float(value)

    @property
    def windWaveUpperFrequency(self) -> float:
        """Wind wave upper frequency limit"""
        return self.__windWaveUpperFrequency

    @windWaveUpperFrequency.setter
    def windWaveUpperFrequency(self, value: float):
        """Set windWaveUpperFrequency"""
        self.__windWaveUpperFrequency = float(value)

    @property
    def swellWaveLowerFrequency(self) -> float:
        """Swell wave lower frequency limit"""
        return self.__swellWaveLowerFrequency

    @swellWaveLowerFrequency.setter
    def swellWaveLowerFrequency(self, value: float):
        """Set swellWaveLowerFrequency"""
        self.__swellWaveLowerFrequency = float(value)

    @property
    def swellWaveUpperFrequency(self) -> float:
        """Swell wave upper frequency limit"""
        return self.__swellWaveUpperFrequency

    @swellWaveUpperFrequency.setter
    def swellWaveUpperFrequency(self, value: float):
        """Set swellWaveUpperFrequency"""
        self.__swellWaveUpperFrequency = float(value)

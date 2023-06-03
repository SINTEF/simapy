# This an autogenerated file
# 
# Generated with HawserForceMeasurement
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hawserforcemeasurement import HawserForceMeasurementBlueprint
from typing import Dict
from sima.sima import MOAO
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simplecoupling import SimpleCoupling

class HawserForceMeasurement(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    standardDeviation : float
         White noise standard deviation of the measurement system(default 0.0)
    seed : int
         Seed number for the realisation of the white noise(default 1)
    coupling : SimpleCoupling
    """

    def __init__(self , description="", standardDeviation=0.0, seed=1, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.standardDeviation = standardDeviation
        self.seed = seed
        self.coupling = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HawserForceMeasurementBlueprint()


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
    def standardDeviation(self) -> float:
        """White noise standard deviation of the measurement system"""
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, value: float):
        """Set standardDeviation"""
        self.__standardDeviation = float(value)

    @property
    def seed(self) -> int:
        """Seed number for the realisation of the white noise"""
        return self.__seed

    @seed.setter
    def seed(self, value: int):
        """Set seed"""
        self.__seed = int(value)

    @property
    def coupling(self) -> SimpleCoupling:
        """"""
        return self.__coupling

    @coupling.setter
    def coupling(self, value: SimpleCoupling):
        """Set coupling"""
        self.__coupling = value

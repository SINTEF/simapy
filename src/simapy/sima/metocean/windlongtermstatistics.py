# This an autogenerated file
# 
# Generated with WindLongTermStatistics
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.windlongtermstatistics import WindLongTermStatisticsBlueprint
from typing import Dict
from ..sima import Named
from ..sima import ScriptableValue
from .levelextreme import LevelExtreme
from .weibulldistribution import WeibullDistribution

class WindLongTermStatistics(Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    weibullDistributions : List[WeibullDistribution]
    extremes : List[LevelExtreme]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.weibullDistributions = list()
        self.extremes = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WindLongTermStatisticsBlueprint()


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
    def weibullDistributions(self) -> List[WeibullDistribution]:
        """"""
        return self.__weibullDistributions

    @weibullDistributions.setter
    def weibullDistributions(self, value: List[WeibullDistribution]):
        """Set weibullDistributions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__weibullDistributions = value

    @property
    def extremes(self) -> List[LevelExtreme]:
        """"""
        return self.__extremes

    @extremes.setter
    def extremes(self, value: List[LevelExtreme]):
        """Set extremes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__extremes = value

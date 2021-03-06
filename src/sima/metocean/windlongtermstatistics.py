# This an autogenerated file
# 
# Generated with WindLongTermStatistics
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.windlongtermstatistics import WindLongTermStatisticsBlueprint
from typing import Dict
from sima.metocean.levelextreme import LevelExtreme
from sima.metocean.weibulldistribution import WeibullDistribution
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class WindLongTermStatistics(MOAO):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    weibullDistributions : List[WeibullDistribution]
    extremes : List[LevelExtreme]
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

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
    def weibullDistributions(self) -> List[WeibullDistribution]:
        """"""
        return self.__weibullDistributions

    @weibullDistributions.setter
    def weibullDistributions(self, value: List[WeibullDistribution]):
        """Set weibullDistributions"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__weibullDistributions = value

    @property
    def extremes(self) -> List[LevelExtreme]:
        """"""
        return self.__extremes

    @extremes.setter
    def extremes(self, value: List[LevelExtreme]):
        """Set extremes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__extremes = value

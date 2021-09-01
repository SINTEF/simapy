# This an autogenerated file
# 
# Generated with DirectionDependentWeibullDistribution
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.directiondependentweibulldistribution import DirectionDependentWeibullDistributionBlueprint
from sima.metocean.weibulldistribution import WeibullDistribution
from sima.metocean.weibulldistributionitem import WeibullDistributionItem
from sima.sima.scriptablevalue import ScriptableValue

class DirectionDependentWeibullDistribution(WeibullDistribution):
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
    returnPeriod : float
         (default 0.0)
    level : float
         (default 0.0)
    duration : float
         (default 0.0)
    items : List[WeibullDistributionItem]
    """

    def __init__(self , name:str="", description:str="", _id:str="", returnPeriod:float=0.0, level:float=0.0, duration:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__returnPeriod = returnPeriod
        self.__level = level
        self.__duration = duration
        self.__items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DirectionDependentWeibullDistributionBlueprint()


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
    def returnPeriod(self) -> float:
        """"""
        return self.__returnPeriod

    @returnPeriod.setter
    def returnPeriod(self, value: float):
        """Set returnPeriod"""
        self.__returnPeriod = float(value)

    @property
    def level(self) -> float:
        """"""
        return self.__level

    @level.setter
    def level(self, value: float):
        """Set level"""
        self.__level = float(value)

    @property
    def duration(self) -> float:
        """"""
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        """Set duration"""
        self.__duration = float(value)

    @property
    def items(self) -> List[WeibullDistributionItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[WeibullDistributionItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value

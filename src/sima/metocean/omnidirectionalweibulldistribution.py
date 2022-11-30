# This an autogenerated file
# 
# Generated with OmniDirectionalWeibullDistribution
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.omnidirectionalweibulldistribution import OmniDirectionalWeibullDistributionBlueprint
from typing import Dict
from sima.metocean.weibulldistribution import WeibullDistribution
from sima.sima.scriptablevalue import ScriptableValue

class OmniDirectionalWeibullDistribution(WeibullDistribution):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    returnPeriod : float
         (default 0.0)
    level : float
         (default 0.0)
    duration : float
         (default 0.0)
    probability : float
         (default 0.0)
    shape : float
         (default 0.0)
    scale : float
         (default 0.0)
    location : float
         (default 0.0)
    """

    def __init__(self , description="", returnPeriod=0.0, level=0.0, duration=0.0, probability=0.0, shape=0.0, scale=0.0, location=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.returnPeriod = returnPeriod
        self.level = level
        self.duration = duration
        self.probability = probability
        self.shape = shape
        self.scale = scale
        self.location = location
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OmniDirectionalWeibullDistributionBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

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
    def probability(self) -> float:
        """"""
        return self.__probability

    @probability.setter
    def probability(self, value: float):
        """Set probability"""
        self.__probability = float(value)

    @property
    def shape(self) -> float:
        """"""
        return self.__shape

    @shape.setter
    def shape(self, value: float):
        """Set shape"""
        self.__shape = float(value)

    @property
    def scale(self) -> float:
        """"""
        return self.__scale

    @scale.setter
    def scale(self, value: float):
        """Set scale"""
        self.__scale = float(value)

    @property
    def location(self) -> float:
        """"""
        return self.__location

    @location.setter
    def location(self, value: float):
        """Set location"""
        self.__location = float(value)

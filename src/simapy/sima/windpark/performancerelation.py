# This an autogenerated file
# 
# Generated with PerformanceRelation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.performancerelation import PerformanceRelationBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .performancerelationitem import PerformanceRelationItem

class PerformanceRelation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    yawAngle : float
         Yaw misalignment(default 0.0)
    items : List[PerformanceRelationItem]
    """

    def __init__(self , description="", yawAngle=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.yawAngle = yawAngle
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PerformanceRelationBlueprint()


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
    def yawAngle(self) -> float:
        """Yaw misalignment"""
        return self.__yawAngle

    @yawAngle.setter
    def yawAngle(self, value: float):
        """Set yawAngle"""
        self.__yawAngle = float(value)

    @property
    def items(self) -> List[PerformanceRelationItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[PerformanceRelationItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__items = value
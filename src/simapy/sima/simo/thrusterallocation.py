# This an autogenerated file
# 
# Generated with ThrusterAllocation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thrusterallocation import ThrusterAllocationBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .ithruster import IThruster

class ThrusterAllocation(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    weight : float
         Factor in weight function for thruster allocation(default 1.0)
    thruster : IThruster
         Thruster controlled by the allocation system
    """

    def __init__(self , description="", weight=1.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.weight = weight
        self.thruster = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterAllocationBlueprint()


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
    def weight(self) -> float:
        """Factor in weight function for thruster allocation"""
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        """Set weight"""
        self.__weight = float(value)

    @property
    def thruster(self) -> IThruster:
        """Thruster controlled by the allocation system"""
        return self.__thruster

    @thruster.setter
    def thruster(self, value: IThruster):
        """Set thruster"""
        self.__thruster = value

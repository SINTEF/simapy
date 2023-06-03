# This an autogenerated file
# 
# Generated with ThrusterReduction
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thrusterreduction import ThrusterReductionBlueprint
from typing import Dict
from sima.sima import MOAO
from sima.sima import ScriptableValue

class ThrusterReduction(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    propellerDirection : float
         Direction of propeller axis in body coordinate system(default 0.0)
    reductionFactor : float
         Thrust reduction factor(default 1.0)
    """

    def __init__(self , description="", propellerDirection=0.0, reductionFactor=1.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.propellerDirection = propellerDirection
        self.reductionFactor = reductionFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterReductionBlueprint()


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
    def propellerDirection(self) -> float:
        """Direction of propeller axis in body coordinate system"""
        return self.__propellerDirection

    @propellerDirection.setter
    def propellerDirection(self, value: float):
        """Set propellerDirection"""
        self.__propellerDirection = float(value)

    @property
    def reductionFactor(self) -> float:
        """Thrust reduction factor"""
        return self.__reductionFactor

    @reductionFactor.setter
    def reductionFactor(self, value: float):
        """Set reductionFactor"""
        self.__reductionFactor = float(value)

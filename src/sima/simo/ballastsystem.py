# This an autogenerated file
# 
# Generated with BallastSystem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.ballastsystem import BallastSystemBlueprint
from typing import Dict
from .ballasttank import BallastTank
from sima.sima import MOAO
from sima.sima import ScriptableValue

class BallastSystem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    ballastTanks : List[BallastTank]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.ballastTanks = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BallastSystemBlueprint()


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
    def ballastTanks(self) -> List[BallastTank]:
        """"""
        return self.__ballastTanks

    @ballastTanks.setter
    def ballastTanks(self, value: List[BallastTank]):
        """Set ballastTanks"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__ballastTanks = value
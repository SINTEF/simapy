# This an autogenerated file
# 
# Generated with TorsionStiffnessItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.torsionstiffnessitem import TorsionStiffnessItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class TorsionStiffnessItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    torsionMoment : float
         Torsion moment(default 0.0)
    torsionAngle : float
         Torsion angle/length(default 0.0)
    """

    def __init__(self , description="", torsionMoment=0.0, torsionAngle=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.torsionMoment = torsionMoment
        self.torsionAngle = torsionAngle
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TorsionStiffnessItemBlueprint()


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
    def torsionMoment(self) -> float:
        """Torsion moment"""
        return self.__torsionMoment

    @torsionMoment.setter
    def torsionMoment(self, value: float):
        """Set torsionMoment"""
        self.__torsionMoment = float(value)

    @property
    def torsionAngle(self) -> float:
        """Torsion angle/length"""
        return self.__torsionAngle

    @torsionAngle.setter
    def torsionAngle(self, value: float):
        """Set torsionAngle"""
        self.__torsionAngle = float(value)
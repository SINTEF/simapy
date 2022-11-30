# This an autogenerated file
# 
# Generated with BladeItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.bladeitem import BladeItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.windturbine.airfoil import Airfoil

class BladeItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    airfoil : Airfoil
    elementLength : float
         Element length(default 0.0)
    chordLength : float
         Chord length(default 0.0)
    twist : float
         Airfoil twist(default 0.0)
    """

    def __init__(self , description="", elementLength=0.0, chordLength=0.0, twist=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.airfoil = None
        self.elementLength = elementLength
        self.chordLength = chordLength
        self.twist = twist
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BladeItemBlueprint()


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
    def airfoil(self) -> Airfoil:
        """"""
        return self.__airfoil

    @airfoil.setter
    def airfoil(self, value: Airfoil):
        """Set airfoil"""
        self.__airfoil = value

    @property
    def elementLength(self) -> float:
        """Element length"""
        return self.__elementLength

    @elementLength.setter
    def elementLength(self, value: float):
        """Set elementLength"""
        self.__elementLength = float(value)

    @property
    def chordLength(self) -> float:
        """Chord length"""
        return self.__chordLength

    @chordLength.setter
    def chordLength(self, value: float):
        """Set chordLength"""
        self.__chordLength = float(value)

    @property
    def twist(self) -> float:
        """Airfoil twist"""
        return self.__twist

    @twist.setter
    def twist(self, value: float):
        """Set twist"""
        self.__twist = float(value)

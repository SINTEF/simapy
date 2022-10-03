# This an autogenerated file
# 
# Generated with VerticalBladeItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.verticalbladeitem import VerticalBladeItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.windturbine.airfoil import Airfoil

class VerticalBladeItem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    airfoil : Airfoil
    radius : float
         Radius of the second node of the element(default 0.0)
    elevation : float
         Elevation of the second node of the element(default 0.0)
    offset : float
         Offset of the second node of the element from the R-Z plane(default 0.0)
    chordLength : float
         Chord length of the foil profile(default 0.0)
    twist : float
         Static twist angle(default 0.0)
    """

    def __init__(self , _id="", radius=0.0, elevation=0.0, offset=0.0, chordLength=0.0, twist=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.airfoil = None
        self.radius = radius
        self.elevation = elevation
        self.offset = offset
        self.chordLength = chordLength
        self.twist = twist
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VerticalBladeItemBlueprint()


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
    def airfoil(self) -> Airfoil:
        """"""
        return self.__airfoil

    @airfoil.setter
    def airfoil(self, value: Airfoil):
        """Set airfoil"""
        self.__airfoil = value

    @property
    def radius(self) -> float:
        """Radius of the second node of the element"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def elevation(self) -> float:
        """Elevation of the second node of the element"""
        return self.__elevation

    @elevation.setter
    def elevation(self, value: float):
        """Set elevation"""
        self.__elevation = float(value)

    @property
    def offset(self) -> float:
        """Offset of the second node of the element from the R-Z plane"""
        return self.__offset

    @offset.setter
    def offset(self, value: float):
        """Set offset"""
        self.__offset = float(value)

    @property
    def chordLength(self) -> float:
        """Chord length of the foil profile"""
        return self.__chordLength

    @chordLength.setter
    def chordLength(self, value: float):
        """Set chordLength"""
        self.__chordLength = float(value)

    @property
    def twist(self) -> float:
        """Static twist angle"""
        return self.__twist

    @twist.setter
    def twist(self, value: float):
        """Set twist"""
        self.__twist = float(value)

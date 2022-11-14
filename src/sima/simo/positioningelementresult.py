# This an autogenerated file
# 
# Generated with PositioningElementResult
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.positioningelementresult import PositioningElementResultBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.forceresult import ForceResult
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.bodyresult import BodyResult

class PositioningElementResult(ForceResult):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         Force name(default None)
    fx : float
         Statically calculated force(default 0.0)
    fy : float
         Statically calculated force(default 0.0)
    fz : float
         Statically calculated force(default 0.0)
    mx : float
         Statically calculated moment(default 0.0)
    my : float
         Statically calculated moment(default 0.0)
    mz : float
         Statically calculated moment(default 0.0)
    mass : float
         Mass of object(default 0.0)
    bodyResult : BodyResult
    """

    def __init__(self , description="", _id=None, name=None, fx=0.0, fy=0.0, fz=0.0, mx=0.0, my=0.0, mz=0.0, mass=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.mx = mx
        self.my = my
        self.mz = mz
        self.mass = mass
        self.bodyResult = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PositioningElementResultBlueprint()


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
    def name(self) -> str:
        """Force name"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def fx(self) -> float:
        """Statically calculated force"""
        return self.__fx

    @fx.setter
    def fx(self, value: float):
        """Set fx"""
        self.__fx = float(value)

    @property
    def fy(self) -> float:
        """Statically calculated force"""
        return self.__fy

    @fy.setter
    def fy(self, value: float):
        """Set fy"""
        self.__fy = float(value)

    @property
    def fz(self) -> float:
        """Statically calculated force"""
        return self.__fz

    @fz.setter
    def fz(self, value: float):
        """Set fz"""
        self.__fz = float(value)

    @property
    def mx(self) -> float:
        """Statically calculated moment"""
        return self.__mx

    @mx.setter
    def mx(self, value: float):
        """Set mx"""
        self.__mx = float(value)

    @property
    def my(self) -> float:
        """Statically calculated moment"""
        return self.__my

    @my.setter
    def my(self, value: float):
        """Set my"""
        self.__my = float(value)

    @property
    def mz(self) -> float:
        """Statically calculated moment"""
        return self.__mz

    @mz.setter
    def mz(self, value: float):
        """Set mz"""
        self.__mz = float(value)

    @property
    def mass(self) -> float:
        """Mass of object"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def bodyResult(self) -> BodyResult:
        """"""
        return self.__bodyResult

    @bodyResult.setter
    def bodyResult(self, value: BodyResult):
        """Set bodyResult"""
        self.__bodyResult = value

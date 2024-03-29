# This an autogenerated file
# 
# Generated with DOFElimination
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dofelimination import DOFEliminationBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simobody import SIMOBody

class DOFElimination(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    body : SIMOBody
    x : bool
         Select to omit X degree of freedom(default False)
    y : bool
         Select to omit Y degree of freedom(default False)
    z : bool
         Select to omit Z degree of freedom(default False)
    rx : bool
         Select to omit RX degree of freedom(default False)
    ry : bool
         Select to omit RY degree of freedom(default False)
    rz : bool
         Select to omit RZ degree of freedom(default False)
    """

    def __init__(self , description="", x=False, y=False, z=False, rx=False, ry=False, rz=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.body = None
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DOFEliminationBlueprint()


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
    def body(self) -> SIMOBody:
        """"""
        return self.__body

    @body.setter
    def body(self, value: SIMOBody):
        """Set body"""
        self.__body = value

    @property
    def x(self) -> bool:
        """Select to omit X degree of freedom"""
        return self.__x

    @x.setter
    def x(self, value: bool):
        """Set x"""
        self.__x = bool(value)

    @property
    def y(self) -> bool:
        """Select to omit Y degree of freedom"""
        return self.__y

    @y.setter
    def y(self, value: bool):
        """Set y"""
        self.__y = bool(value)

    @property
    def z(self) -> bool:
        """Select to omit Z degree of freedom"""
        return self.__z

    @z.setter
    def z(self, value: bool):
        """Set z"""
        self.__z = bool(value)

    @property
    def rx(self) -> bool:
        """Select to omit RX degree of freedom"""
        return self.__rx

    @rx.setter
    def rx(self, value: bool):
        """Set rx"""
        self.__rx = bool(value)

    @property
    def ry(self) -> bool:
        """Select to omit RY degree of freedom"""
        return self.__ry

    @ry.setter
    def ry(self, value: bool):
        """Set ry"""
        self.__ry = bool(value)

    @property
    def rz(self) -> bool:
        """Select to omit RZ degree of freedom"""
        return self.__rz

    @rz.setter
    def rz(self, value: bool):
        """Set rz"""
        self.__rz = bool(value)

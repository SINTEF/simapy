# This an autogenerated file
# 
# Generated with Position
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.position import PositionBlueprint
from typing import Dict
from .moao import MOAO
from .scriptablevalue import ScriptableValue

class Position(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    x : float
         x position coordinate (default 0.0)
    y : float
         y position coordinate (default 0.0)
    z : float
         z position coordinate (default 0.0)
    rx : float
         rotation about x-axis(default 0.0)
    ry : float
         rotation about y-axis(default 0.0)
    rz : float
         rotation about z-axis(default 0.0)
    """

    def __init__(self , description="", x=0.0, y=0.0, z=0.0, rx=0.0, ry=0.0, rz=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
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
        return PositionBlueprint()


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
    def x(self) -> float:
        """x position coordinate """
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """y position coordinate """
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def z(self) -> float:
        """z position coordinate """
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)

    @property
    def rx(self) -> float:
        """rotation about x-axis"""
        return self.__rx

    @rx.setter
    def rx(self, value: float):
        """Set rx"""
        self.__rx = float(value)

    @property
    def ry(self) -> float:
        """rotation about y-axis"""
        return self.__ry

    @ry.setter
    def ry(self, value: float):
        """Set ry"""
        self.__ry = float(value)

    @property
    def rz(self) -> float:
        """rotation about z-axis"""
        return self.__rz

    @rz.setter
    def rz(self, value: float):
        """Set rz"""
        self.__rz = float(value)
# This an autogenerated file
# 
# Generated with XYItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.xyitem import XYItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class XYItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    x : float
         (default 0.0)
    y : float
         (default 0.0)
    """

    def __init__(self , description="", x=0.0, y=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.x = x
        self.y = y
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return XYItemBlueprint()


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
    def x(self) -> float:
        """"""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

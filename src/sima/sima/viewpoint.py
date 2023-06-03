# This an autogenerated file
# 
# Generated with Viewpoint
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.viewpoint import ViewpointBlueprint
from typing import Dict
from .moao import MOAO
from .point3 import Point3
from .scriptablevalue import ScriptableValue
from .vector3 import Vector3

class Viewpoint(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    eye : Point3
    dir : Vector3
    up : Vector3
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.eye = None
        self.dir = None
        self.up = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ViewpointBlueprint()


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
    def eye(self) -> Point3:
        """"""
        return self.__eye

    @eye.setter
    def eye(self, value: Point3):
        """Set eye"""
        self.__eye = value

    @property
    def dir(self) -> Vector3:
        """"""
        return self.__dir

    @dir.setter
    def dir(self, value: Vector3):
        """Set dir"""
        self.__dir = value

    @property
    def up(self) -> Vector3:
        """"""
        return self.__up

    @up.setter
    def up(self, value: Vector3):
        """Set up"""
        self.__up = value

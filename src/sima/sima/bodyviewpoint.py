# This an autogenerated file
# 
# Generated with BodyViewpoint
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.bodyviewpoint import BodyViewpointBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.vector3 import Vector3
from sima.sima.viewpoint import Viewpoint

class BodyViewpoint(Viewpoint,NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    eye : Point3
    dir : Vector3
    up : Vector3
    name : str
         (default None)
    """

    def __init__(self , description="", _id=None, name=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.eye = None
        self.dir = None
        self.up = None
        self.name = name
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BodyViewpointBlueprint()


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

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

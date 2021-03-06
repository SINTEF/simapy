# This an autogenerated file
# 
# Generated with WindParkTurbine
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.windparkturbine import WindParkTurbineBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.windpark.windturbinetype import WindTurbineType

class WindParkTurbine(NamedObject):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    _type : WindTurbineType
    x : float
         Global x-coordinate of the hub(default 0.0)
    y : float
         Global y-coordinate of the hub(default 0.0)
    z : float
         Global z-coordinate of the hub(default 0.0)
    shaftAngle : float
         (default 0.0)
    target : bool
         (default False)
    """

    def __init__(self , name="", description="", _id="", x=0.0, y=0.0, z=0.0, shaftAngle=0.0, target=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self._type = None
        self.x = x
        self.y = y
        self.z = z
        self.shaftAngle = shaftAngle
        self.target = target
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WindParkTurbineBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def _type(self) -> WindTurbineType:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: WindTurbineType):
        """Set _type"""
        self.___type = value

    @property
    def x(self) -> float:
        """Global x-coordinate of the hub"""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """Global y-coordinate of the hub"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def z(self) -> float:
        """Global z-coordinate of the hub"""
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)

    @property
    def shaftAngle(self) -> float:
        """"""
        return self.__shaftAngle

    @shaftAngle.setter
    def shaftAngle(self, value: float):
        """Set shaftAngle"""
        self.__shaftAngle = float(value)

    @property
    def target(self) -> bool:
        """"""
        return self.__target

    @target.setter
    def target(self, value: bool):
        """Set target"""
        self.__target = bool(value)

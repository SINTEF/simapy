# This an autogenerated file
# 
# Generated with ExcitationZoneProperty
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.excitationzoneproperty import ExcitationZonePropertyBlueprint
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class ExcitationZoneProperty(NamedObject):
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
    min : float
         Minimum non dimensional frequency limit(default 0.125)
    max : float
         Minimum non dimensional frequency limit(default 0.2)
    """

    def __init__(self , name:str="", description:str="", _id:str="", min:float=0.125, max:float=0.2, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__min = min
        self.__max = max
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExcitationZonePropertyBlueprint()


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
    def min(self) -> float:
        """Minimum non dimensional frequency limit"""
        return self.__min

    @min.setter
    def min(self, value: float):
        """Set min"""
        self.__min = float(value)

    @property
    def max(self) -> float:
        """Minimum non dimensional frequency limit"""
        return self.__max

    @max.setter
    def max(self, value: float):
        """Set max"""
        self.__max = float(value)

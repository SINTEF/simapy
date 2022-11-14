# This an autogenerated file
# 
# Generated with Range
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.range import RangeBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class Range(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    min : float
         (default 0.0)
    max : float
         (default 0.0)
    automatic : bool
         (default False)
    """

    def __init__(self , description="", _id=None, min=0.0, max=0.0, automatic=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.min = min
        self.max = max
        self.automatic = automatic
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RangeBlueprint()


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
        """"""
        return self.__min

    @min.setter
    def min(self, value: float):
        """Set min"""
        self.__min = float(value)

    @property
    def max(self) -> float:
        """"""
        return self.__max

    @max.setter
    def max(self, value: float):
        """Set max"""
        self.__max = float(value)

    @property
    def automatic(self) -> bool:
        """"""
        return self.__automatic

    @automatic.setter
    def automatic(self, value: bool):
        """Set automatic"""
        self.__automatic = bool(value)

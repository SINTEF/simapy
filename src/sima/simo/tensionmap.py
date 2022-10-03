# This an autogenerated file
# 
# Generated with TensionMap
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.tensionmap import TensionMapBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.distancekey import DistanceKey
from sima.simo.tensionitem import TensionItem

class TensionMap(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    key : DistanceKey
    value : TensionItem
    """

    def __init__(self , _id="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.key = None
        self.value = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TensionMapBlueprint()


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
    def key(self) -> DistanceKey:
        """"""
        return self.__key

    @key.setter
    def key(self, value: DistanceKey):
        """Set key"""
        self.__key = value

    @property
    def value(self) -> TensionItem:
        """"""
        return self.__value

    @value.setter
    def value(self, value: TensionItem):
        """Set value"""
        self.__value = value

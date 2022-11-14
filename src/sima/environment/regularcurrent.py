# This an autogenerated file
# 
# Generated with RegularCurrent
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.regularcurrent import RegularCurrentBlueprint
from typing import Dict
from sima.environment.current import Current
from sima.environment.currentitem import CurrentItem
from sima.sima.scriptablevalue import ScriptableValue

class RegularCurrent(Current):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    items : List[CurrentItem]
    """

    def __init__(self , description="", _id=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RegularCurrentBlueprint()


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
    def items(self) -> List[CurrentItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[CurrentItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value

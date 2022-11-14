# This an autogenerated file
# 
# Generated with StringIntItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stringintitem import StringIntItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class StringIntItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    text : str
         (default None)
    value : int
         (default 0)
    """

    def __init__(self , description="", _id=None, text=None, value=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.text = text
        self.value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StringIntItemBlueprint()


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
    def text(self) -> str:
        """"""
        return self.__text

    @text.setter
    def text(self, value: str):
        """Set text"""
        self.__text = str(value)

    @property
    def value(self) -> int:
        """"""
        return self.__value

    @value.setter
    def value(self, value: int):
        """Set value"""
        self.__value = int(value)

# This an autogenerated file
# 
# Generated with QTFDofItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.qtfdofitem import QTFDofItemBlueprint
from typing import Dict
from .qtfvalue import QTFValue
from sima.sima import MOAO
from sima.sima import ScriptableValue

class QTFDofItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    values : List[QTFValue]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.values = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return QTFDofItemBlueprint()


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
    def values(self) -> List[QTFValue]:
        """"""
        return self.__values

    @values.setter
    def values(self, value: List[QTFValue]):
        """Set values"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__values = value
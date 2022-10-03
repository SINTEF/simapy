# This an autogenerated file
# 
# Generated with DynamicCurrentVariation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamiccurrentvariation import DynamicCurrentVariationBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class DynamicCurrentVariation(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    active : bool
         (default True)
    fileName : str
         File name for dynamic current variation(default "")
    """

    def __init__(self , _id="", active=True, fileName="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.active = active
        self.fileName = fileName
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicCurrentVariationBlueprint()


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
    def active(self) -> bool:
        """"""
        return self.__active

    @active.setter
    def active(self, value: bool):
        """Set active"""
        self.__active = bool(value)

    @property
    def fileName(self) -> str:
        """File name for dynamic current variation"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = str(value)

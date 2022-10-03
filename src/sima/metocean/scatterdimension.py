# This an autogenerated file
# 
# Generated with ScatterDimension
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scatterdimension import ScatterDimensionBlueprint
from numpy import ndarray,asarray
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ScatterDimension(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    nValues : int
         (default 0)
    values : ndarray
         Scatter values
    """

    def __init__(self , _id="", nValues=0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.nValues = nValues
        self.values = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScatterDimensionBlueprint()


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
    def nValues(self) -> int:
        """"""
        return self.__nValues

    @nValues.setter
    def nValues(self, value: int):
        """Set nValues"""
        self.__nValues = int(value)

    @property
    def values(self) -> ndarray:
        """Scatter values"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        self.__values = asarray(value)

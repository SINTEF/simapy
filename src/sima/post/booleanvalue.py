# This an autogenerated file
# 
# Generated with BooleanValue
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.booleanvalue import BooleanValueBlueprint
from numpy import ndarray,asarray
from sima.post.generatorsignal import GeneratorSignal
from sima.post.signalproperties import SignalProperties
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.singleparameter import SingleParameter

class BooleanValue(GeneratorSignal,SingleParameter):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    properties : List[SignalProperties]
    name : str
         (default "")
    array : bool
         (default False)
    value : bool
         (default False)
    values : ndarray
         Value of the String constant
    """

    def __init__(self , _id="", name="", array=False, value=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.properties = list()
        self.name = name
        self.array = array
        self.value = value
        self.values = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BooleanValueBlueprint()


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
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def array(self) -> bool:
        """"""
        return self.__array

    @array.setter
    def array(self, value: bool):
        """Set array"""
        self.__array = bool(value)

    @property
    def value(self) -> bool:
        """"""
        return self.__value

    @value.setter
    def value(self, value: bool):
        """Set value"""
        self.__value = bool(value)

    @property
    def values(self) -> ndarray:
        """Value of the String constant"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        self.__values = asarray(value)

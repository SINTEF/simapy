# This an autogenerated file
# 
# Generated with NumberSignalInputSlot
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.numbersignalinputslot import NumberSignalInputSlotBlueprint
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.signalproperties import SignalProperties
from sima.sima.scriptablevalue import ScriptableValue

class NumberSignalInputSlot(ControlSignalInputSlot):
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
    properties : List[SignalProperties]
    specifyAdditionalProperties : bool
         Specify additional properties in the signal(default False)
    array : bool
         (default False)
    value : float
         (default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", specifyAdditionalProperties:bool=False, array:bool=False, value:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__properties = list()
        self.__specifyAdditionalProperties = specifyAdditionalProperties
        self.__array = array
        self.__value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NumberSignalInputSlotBlueprint()


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
    def specifyAdditionalProperties(self) -> bool:
        """Specify additional properties in the signal"""
        return self.__specifyAdditionalProperties

    @specifyAdditionalProperties.setter
    def specifyAdditionalProperties(self, value: bool):
        """Set specifyAdditionalProperties"""
        self.__specifyAdditionalProperties = bool(value)

    @property
    def array(self) -> bool:
        """"""
        return self.__array

    @array.setter
    def array(self, value: bool):
        """Set array"""
        self.__array = bool(value)

    @property
    def value(self) -> float:
        """"""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Set value"""
        self.__value = float(value)

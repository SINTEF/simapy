# This an autogenerated file
# 
# Generated with TextSignalInputSlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.textsignalinputslot import TextSignalInputSlotBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .controlsignalinputslot import ControlSignalInputSlot
from .signalproperties import SignalProperties

class TextSignalInputSlot(ControlSignalInputSlot):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[SignalProperties]
    specifyAdditionalProperties : bool
         Specify additional properties in the signal(default False)
    array : bool
         (default False)
    value : str
         (default None)
    """

    def __init__(self , description="", specifyAdditionalProperties=False, array=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.specifyAdditionalProperties = specifyAdditionalProperties
        self.array = array
        self.value = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TextSignalInputSlotBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
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
    def value(self) -> str:
        """"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = value
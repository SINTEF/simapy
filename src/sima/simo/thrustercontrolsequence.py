# This an autogenerated file
# 
# Generated with ThrusterControlSequence
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.thrustercontrolsequence import ThrusterControlSequenceBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.controlsequenceitem import ControlSequenceItem
from sima.simo.thrustsignaltype import ThrustSignalType

class ThrusterControlSequence(MOAO):
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
    specifyControlSequence : bool
         Should a list of control signals be specified for thruster?(default False)
    signalType : ThrustSignalType
         Unit for demanded thrust force
    items : List[ControlSequenceItem]
    """

    def __init__(self , name:str="", description:str="", _id:str="", specifyControlSequence:bool=False, signalType:ThrustSignalType=ThrustSignalType.FORCE, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__specifyControlSequence = specifyControlSequence
        self.__signalType = signalType
        self.__items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterControlSequenceBlueprint()


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
    def specifyControlSequence(self) -> bool:
        """Should a list of control signals be specified for thruster?"""
        return self.__specifyControlSequence

    @specifyControlSequence.setter
    def specifyControlSequence(self, value: bool):
        """Set specifyControlSequence"""
        self.__specifyControlSequence = bool(value)

    @property
    def signalType(self) -> ThrustSignalType:
        """Unit for demanded thrust force"""
        return self.__signalType

    @signalType.setter
    def signalType(self, value: ThrustSignalType):
        """Set signalType"""
        self.__signalType = value

    @property
    def items(self) -> List[ControlSequenceItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[ControlSequenceItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value

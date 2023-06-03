# This an autogenerated file
# 
# Generated with ThrusterControlSequence
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thrustercontrolsequence import ThrusterControlSequenceBlueprint
from typing import Dict
from .controlsequenceitem import ControlSequenceItem
from .thrustsignaltype import ThrustSignalType
from sima.sima import MOAO
from sima.sima import ScriptableValue

class ThrusterControlSequence(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    specifyControlSequence : bool
         Should a list of control signals be specified for thruster?(default False)
    signalType : ThrustSignalType
         Unit for demanded thrust force
    items : List[ControlSequenceItem]
    """

    def __init__(self , description="", specifyControlSequence=False, signalType=ThrustSignalType.FORCE, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.specifyControlSequence = specifyControlSequence
        self.signalType = signalType
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterControlSequenceBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__items = value

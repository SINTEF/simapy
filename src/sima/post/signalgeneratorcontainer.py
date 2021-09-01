# This an autogenerated file
# 
# Generated with SignalGeneratorContainer
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.signalgeneratorcontainer import SignalGeneratorContainerBlueprint
from sima.post.generatorsignal import GeneratorSignal
from sima.post.signalproperties import SignalProperties
from sima.post.signalpropertiescontainer import SignalPropertiesContainer
from sima.sima.scriptablevalue import ScriptableValue

class SignalGeneratorContainer(SignalPropertiesContainer):
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
    signals : List[GeneratorSignal]
    children : List[SignalGeneratorContainer]
    """

    def __init__(self , name:str="", description:str="", _id:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__properties = list()
        self.__signals = list()
        self.__children = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SignalGeneratorContainerBlueprint()


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
    def signals(self) -> List[GeneratorSignal]:
        """"""
        return self.__signals

    @signals.setter
    def signals(self, value: List[GeneratorSignal]):
        """Set signals"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__signals = value

    @property
    def children(self) -> List[SignalGeneratorContainer]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[SignalGeneratorContainer]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__children = value

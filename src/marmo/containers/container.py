# This an autogenerated file
# Containers contain signals and other containers
# Generated with Container
from __future__ import annotations
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.container import ContainerBlueprint
from typing import Dict,Sequence,List
from marmo.containers.attribute import Attribute
from marmo.containers.signal import Signal

class Container(Entity):
    """
    Containers contain signals and other containers
    
    Keyword arguments
    -----------------
    name : str 
         (default "")
    description : str 
         (default "")
    attributes : List[Attribute] 
         
    signals : List[Signal] 
         
    containers : List[Container] 
         
    """

    def __init__(self , name:str="", description:str="", **kwargs):
        self.__name = name
        self.__description = description
        self.__attributes = list()
        self.__signals = list()
        self.__containers = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ContainerBlueprint()


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
    def attributes(self) -> List[Attribute]:
        """"""
        return self.__attributes

    @attributes.setter
    def attributes(self, value: List[Attribute]):
        """Set attributes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__attributes = value

    @property
    def signals(self) -> List[Signal]:
        """"""
        return self.__signals

    @signals.setter
    def signals(self, value: List[Signal]):
        """Set signals"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__signals = value

    @property
    def containers(self) -> List[Container]:
        """"""
        return self.__containers

    @containers.setter
    def containers(self, value: List[Container]):
        """Set containers"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__containers = value

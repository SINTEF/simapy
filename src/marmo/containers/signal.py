# This an autogenerated file
# Signal base type
# Generated with Signal
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.signal import SignalBlueprint
from typing import Dict
from marmo.containers.attribute import Attribute
from marmo.containers.signalitem import SignalItem

class Signal(SignalItem):
    """
    Signal base type
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    attributes : List[Attribute]
    """

    def __init__(self , name="", description="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.attributes = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SignalBlueprint()


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

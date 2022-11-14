# This an autogenerated file
# 
# Generated with SimpleString
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simplestring import SimpleStringBlueprint
from typing import Dict
from marmo.containers.attribute import Attribute
from marmo.containers.signal import Signal

class SimpleString(Signal):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         (default None)
    attributes : List[Attribute]
    value : str
         (default None)
    """

    def __init__(self , description="", name=None, value=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = name
        self.attributes = list()
        self.value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SimpleStringBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def value(self) -> str:
        """"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = str(value)

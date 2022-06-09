# This an autogenerated file
# 2D matrix of values with dimension
# Generated with DimensionalMatrix
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dimensionalmatrix import DimensionalMatrixBlueprint
from numpy import ndarray,asarray
from marmo.containers.attribute import Attribute
from marmo.containers.signal import Signal

class DimensionalMatrix(Signal):
    """
    2D matrix of values with dimension
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    attributes : List[Attribute]
    value : ndarray
    label : str
         (default "")
    unit : ndarray
    """

    def __init__(self , name="", description="", label="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.attributes = list()
        self.value = ndarray(2)
        self.label = label
        self.unit = ndarray(2)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DimensionalMatrixBlueprint()


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
    def value(self) -> ndarray:
        """"""
        return self.__value

    @value.setter
    def value(self, value: ndarray):
        """Set value"""
        self.__value = asarray(value)

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def unit(self) -> ndarray:
        """"""
        return self.__unit

    @unit.setter
    def unit(self, value: ndarray):
        """Set unit"""
        self.__unit = asarray(value)

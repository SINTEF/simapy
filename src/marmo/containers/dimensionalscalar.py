# This an autogenerated file
# Single scalar value with dimension
# Generated with DimensionalScalar
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dimensionalscalar import DimensionalScalarBlueprint
from typing import Dict
from marmo.containers.attribute import Attribute
from marmo.containers.signal import Signal

class DimensionalScalar(Signal):
    """
    Single scalar value with dimension
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    attributes : List[Attribute]
    value : float
         (default 0.0)
    label : str
         (default "")
    unit : str
         (default "")
    """

    def __init__(self , name="", description="", value=0.0, label="", unit="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.attributes = list()
        self.value = value
        self.label = label
        self.unit = unit
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DimensionalScalarBlueprint()


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
    def value(self) -> float:
        """"""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Set value"""
        self.__value = float(value)

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def unit(self) -> str:
        """"""
        return self.__unit

    @unit.setter
    def unit(self, value: str):
        """Set unit"""
        self.__unit = str(value)

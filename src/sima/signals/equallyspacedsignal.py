# This an autogenerated file
# Data model for an equally spaced signal.
# Generated with EquallySpacedSignal
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.equallyspacedsignal import EquallySpacedSignalBlueprint
from numpy import ndarray,asarray
from .attribute import Attribute
from .signal import Signal

class EquallySpacedSignal(Signal):
    """
    Data model for an equally spaced signal.
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         (default None)
    attributes : List[Attribute]
    value : ndarray of float
    xstart : float
         (default 0.0)
    xdelta : float
         (default 1.0)
    unit : str
         (default None)
    xunit : str
         (default None)
    xname : str
         (default None)
    xlabel : str
         (default None)
    xdescription : str
         (default None)
    label : str
         (default None)
    legend : str
         (default None)
    """

    def __init__(self , description="", xstart=0.0, xdelta=1.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = None
        self.attributes = list()
        self.value = []
        self.xstart = xstart
        self.xdelta = xdelta
        self.unit = None
        self.xunit = None
        self.xname = None
        self.xlabel = None
        self.xdescription = None
        self.label = None
        self.legend = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return EquallySpacedSignalBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def attributes(self) -> List[Attribute]:
        """"""
        return self.__attributes

    @attributes.setter
    def attributes(self, value: List[Attribute]):
        """Set attributes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__attributes = value

    @property
    def value(self) -> ndarray:
        """"""
        return self.__value

    @value.setter
    def value(self, value: ndarray):
        """Set value"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__value = array

    @property
    def xstart(self) -> float:
        """"""
        return self.__xstart

    @xstart.setter
    def xstart(self, value: float):
        """Set xstart"""
        self.__xstart = float(value)

    @property
    def xdelta(self) -> float:
        """"""
        return self.__xdelta

    @xdelta.setter
    def xdelta(self, value: float):
        """Set xdelta"""
        self.__xdelta = float(value)

    @property
    def unit(self) -> str:
        """"""
        return self.__unit

    @unit.setter
    def unit(self, value: str):
        """Set unit"""
        self.__unit = value

    @property
    def xunit(self) -> str:
        """"""
        return self.__xunit

    @xunit.setter
    def xunit(self, value: str):
        """Set xunit"""
        self.__xunit = value

    @property
    def xname(self) -> str:
        """"""
        return self.__xname

    @xname.setter
    def xname(self, value: str):
        """Set xname"""
        self.__xname = value

    @property
    def xlabel(self) -> str:
        """"""
        return self.__xlabel

    @xlabel.setter
    def xlabel(self, value: str):
        """Set xlabel"""
        self.__xlabel = value

    @property
    def xdescription(self) -> str:
        """"""
        return self.__xdescription

    @xdescription.setter
    def xdescription(self, value: str):
        """Set xdescription"""
        self.__xdescription = value

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = value

    @property
    def legend(self) -> str:
        """"""
        return self.__legend

    @legend.setter
    def legend(self, value: str):
        """Set legend"""
        self.__legend = value
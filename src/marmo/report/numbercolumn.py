# This an autogenerated file
# 
# Generated with NumberColumn
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.numbercolumn import NumberColumnBlueprint
from numpy import ndarray,asarray
from marmo.report.column import Column
from marmo.report.font import Font

class NumberColumn(Column):
    """
    Keyword arguments
    -----------------
    header : str
         (default "")
    label : str
         (default "")
    headerfont : Font
    cells : ndarray
    format : str
         (default "")
    """

    def __init__(self , header="", label="", format="", **kwargs):
        super().__init__(**kwargs)
        self.header = header
        self.label = label
        self.headerfont = None
        self.cells = ndarray(1)
        self.format = format
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NumberColumnBlueprint()


    @property
    def header(self) -> str:
        """"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = str(value)

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def headerfont(self) -> Font:
        """"""
        return self.__headerfont

    @headerfont.setter
    def headerfont(self, value: Font):
        """Set headerfont"""
        self.__headerfont = value

    @property
    def cells(self) -> ndarray:
        """"""
        return self.__cells

    @cells.setter
    def cells(self, value: ndarray):
        """Set cells"""
        self.__cells = asarray(value)

    @property
    def format(self) -> str:
        """"""
        return self.__format

    @format.setter
    def format(self, value: str):
        """Set format"""
        self.__format = str(value)

# This an autogenerated file
# 
# Generated with StringColumn
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stringcolumn import StringColumnBlueprint
from numpy import ndarray,asarray
from marmo.report.column import Column
from marmo.report.font import Font

class StringColumn(Column):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    header : str
         (default None)
    label : str
         (default None)
    headerfont : Font
    cells : ndarray
    """

    def __init__(self , description="", header=None, label=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.header = header
        self.label = label
        self.headerfont = None
        self.cells = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StringColumnBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

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

# This an autogenerated file
# 
# Generated with Table
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.table import TableBlueprint
from typing import Dict
from marmo.report.column import Column
from marmo.report.reportitem import ReportItem

class Table(ReportItem):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    caption : str
         (default "")
    transposed : bool
         (default True)
    columns : List[Column]
    """

    def __init__(self , name="", description="", caption="", transposed=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.caption = caption
        self.transposed = transposed
        self.columns = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TableBlueprint()


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
    def caption(self) -> str:
        """"""
        return self.__caption

    @caption.setter
    def caption(self, value: str):
        """Set caption"""
        self.__caption = str(value)

    @property
    def transposed(self) -> bool:
        """"""
        return self.__transposed

    @transposed.setter
    def transposed(self, value: bool):
        """Set transposed"""
        self.__transposed = bool(value)

    @property
    def columns(self) -> List[Column]:
        """"""
        return self.__columns

    @columns.setter
    def columns(self, value: List[Column]):
        """Set columns"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__columns = value

# This an autogenerated file
# 
# Generated with Table
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.table import TableBlueprint
from typing import Dict
from .column import Column
from .reportitem import ReportItem

class Table(ReportItem):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    caption : str
         (default None)
    transposed : bool
         (default False)
    columns : List[Column]
    """

    def __init__(self , description="", transposed=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.caption = None
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
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def caption(self) -> str:
        """"""
        return self.__caption

    @caption.setter
    def caption(self, value: str):
        """Set caption"""
        self.__caption = value

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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__columns = value

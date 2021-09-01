# This an autogenerated file
# 
# Generated with Table
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.table import TableBlueprint
from sima.report.reportitem import ReportItem
from sima.report.tablecolumn import TableColumn
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class Table(ReportItem):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    object : MOAO
    caption : str
         Caption(default "")
    autoSplit : bool
         Automatically split a large table into multiple tables.(default True)
    columns : List[TableColumn]
    customisableTable : bool
         (default False)
    """

    def __init__(self , name:str="", description:str="", _id:str="", caption:str="", autoSplit:bool=True, customisableTable:bool=False, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__object = None
        self.__caption = caption
        self.__autoSplit = autoSplit
        self.__columns = list()
        self.__customisableTable = customisableTable
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
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def object(self) -> MOAO:
        """"""
        return self.__object

    @object.setter
    def object(self, value: MOAO):
        """Set object"""
        self.__object = value

    @property
    def caption(self) -> str:
        """Caption"""
        return self.__caption

    @caption.setter
    def caption(self, value: str):
        """Set caption"""
        self.__caption = str(value)

    @property
    def autoSplit(self) -> bool:
        """Automatically split a large table into multiple tables."""
        return self.__autoSplit

    @autoSplit.setter
    def autoSplit(self, value: bool):
        """Set autoSplit"""
        self.__autoSplit = bool(value)

    @property
    def columns(self) -> List[TableColumn]:
        """"""
        return self.__columns

    @columns.setter
    def columns(self, value: List[TableColumn]):
        """Set columns"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__columns = value

    @property
    def customisableTable(self) -> bool:
        """"""
        return self.__customisableTable

    @customisableTable.setter
    def customisableTable(self, value: bool):
        """Set customisableTable"""
        self.__customisableTable = bool(value)

# This an autogenerated file
# 
# Generated with TableColumn
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.tablecolumn import TableColumnBlueprint
from typing import Dict
from sima.report.tablecell import TableCell
from sima.report.tablecellstyle import TableCellStyle
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class TableColumn(MOAO):
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
    header : str
         (default "")
    headerStyle : TableCellStyle
    cells : List[TableCell]
    """

    def __init__(self , name="", description="", _id="", header="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.header = header
        self.headerStyle = None
        self.cells = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TableColumnBlueprint()


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
    def header(self) -> str:
        """"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = str(value)

    @property
    def headerStyle(self) -> TableCellStyle:
        """"""
        return self.__headerStyle

    @headerStyle.setter
    def headerStyle(self, value: TableCellStyle):
        """Set headerStyle"""
        self.__headerStyle = value

    @property
    def cells(self) -> List[TableCell]:
        """"""
        return self.__cells

    @cells.setter
    def cells(self, value: List[TableCell]):
        """Set cells"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__cells = value

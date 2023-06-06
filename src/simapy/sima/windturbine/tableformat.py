# Generated with TableFormat
# 
from enum import Enum
from enum import auto

class TableFormat(Enum):
    """"""
    DEFAULT = auto()
    TABLE = auto()

    def label(self):
        if self == TableFormat.DEFAULT:
            return "Default"
        if self == TableFormat.TABLE:
            return "Table"
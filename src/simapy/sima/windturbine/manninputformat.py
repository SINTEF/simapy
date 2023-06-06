# Generated with MannInputFormat
# 
from enum import Enum
from enum import auto

class MannInputFormat(Enum):
    """"""
    DIRECT = auto()
    DERIVED = auto()

    def label(self):
        if self == MannInputFormat.DIRECT:
            return "Direct input"
        if self == MannInputFormat.DERIVED:
            return "Derived input (IEC61400-1)"
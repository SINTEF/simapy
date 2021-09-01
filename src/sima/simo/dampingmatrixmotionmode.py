# Generated with DampingMatrixMotionMode
# 
from enum import Enum
from enum import auto

class DampingMatrixMotionMode(Enum):
    """"""
    DEFAULT = auto()
    TOTAL = auto()
    WF = auto()
    LF = auto()

    def label(self):
        if self == DampingMatrixMotionMode.DEFAULT:
            return "Default"
        if self == DampingMatrixMotionMode.TOTAL:
            return "Total"
        if self == DampingMatrixMotionMode.WF:
            return "Wave frequency"
        if self == DampingMatrixMotionMode.LF:
            return "Low frequency"
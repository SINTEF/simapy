# Generated with IrregularMotionIndicator
# 
from enum import Enum
from enum import auto

class IrregularMotionIndicator(Enum):
    """"""
    STAT = auto()
    NONE = auto()
    FILE = auto()

    def label(self):
        if self == IrregularMotionIndicator.STAT:
            return "Forced irregular motions"
        if self == IrregularMotionIndicator.NONE:
            return "No irregular motions"
        if self == IrregularMotionIndicator.FILE:
            return "Forced irregular motions from file"
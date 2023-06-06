# Generated with CenterOfWinch
# 
from enum import Enum
from enum import auto

class CenterOfWinch(Enum):
    """"""
    NEGATIVE_Z_AXIS = auto()
    POSITIVE_Z_AXIS = auto()

    def label(self):
        if self == CenterOfWinch.NEGATIVE_Z_AXIS:
            return "Negative z-axis"
        if self == CenterOfWinch.POSITIVE_Z_AXIS:
            return "Positive z-axis"
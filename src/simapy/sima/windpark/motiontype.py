# Generated with MotionType
# 
from enum import Enum
from enum import auto

class MotionType(Enum):
    """"""
    POSI = auto()
    DYND = auto()

    def label(self):
        if self == MotionType.POSI:
            return "Global positions"
        if self == MotionType.DYND:
            return "Dynamic displacements"
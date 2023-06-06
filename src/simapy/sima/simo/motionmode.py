# Generated with MotionMode
# 
from enum import Enum
from enum import auto

class MotionMode(Enum):
    """"""
    X = auto()
    Y = auto()
    Z = auto()
    PHI = auto()
    THETA = auto()
    PSI = auto()

    def label(self):
        if self == MotionMode.X:
            return "X"
        if self == MotionMode.Y:
            return "Y"
        if self == MotionMode.Z:
            return "Z"
        if self == MotionMode.PHI:
            return "PHI"
        if self == MotionMode.THETA:
            return "THETA"
        if self == MotionMode.PSI:
            return "PSI"
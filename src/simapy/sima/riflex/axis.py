# Generated with Axis
# 
from enum import Enum
from enum import auto

class Axis(Enum):
    """"""
    X = auto()
    Y = auto()
    Z = auto()

    def label(self):
        if self == Axis.X:
            return "X"
        if self == Axis.Y:
            return "Y"
        if self == Axis.Z:
            return "Z"
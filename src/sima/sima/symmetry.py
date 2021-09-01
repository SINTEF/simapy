# Generated with Symmetry
# 
from enum import Enum
from enum import auto

class Symmetry(Enum):
    """"""
    NONE = auto()
    X = auto()
    Y = auto()
    XY = auto()

    def label(self):
        if self == Symmetry.NONE:
            return "None"
        if self == Symmetry.X:
            return "About X axis"
        if self == Symmetry.Y:
            return "About Y axis"
        if self == Symmetry.XY:
            return "About X and Y axis"
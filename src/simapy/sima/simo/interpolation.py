# Generated with Interpolation
# 
from enum import Enum
from enum import auto

class Interpolation(Enum):
    """"""
    LINEAR = auto()
    PARABOLIC = auto()

    def label(self):
        if self == Interpolation.LINEAR:
            return "Linear"
        if self == Interpolation.PARABOLIC:
            return "Parabolic"
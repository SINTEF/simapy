# Generated with WindMethod
# 
from enum import Enum
from enum import auto

class WindMethod(Enum):
    """"""
    NO_WIND = auto()
    FFT = auto()
    STATE_SPACE = auto()

    def label(self):
        if self == WindMethod.NO_WIND:
            return "No wind"
        if self == WindMethod.FFT:
            return "FFT"
        if self == WindMethod.STATE_SPACE:
            return "State space model"
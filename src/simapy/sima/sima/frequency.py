# Generated with Frequency
# 
from enum import Enum
from enum import auto

class Frequency(Enum):
    """"""
    PERIOD = auto()
    RAD = auto()
    HZ = auto()

    def label(self):
        if self == Frequency.PERIOD:
            return "Period"
        if self == Frequency.RAD:
            return "Rad/s"
        if self == Frequency.HZ:
            return "Hz"
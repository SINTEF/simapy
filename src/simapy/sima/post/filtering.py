# Generated with Filtering
# 
from enum import Enum
from enum import auto

class Filtering(Enum):
    """"""
    NONE = auto()
    LOWPASS = auto()
    HIGHPASS = auto()
    BANDPASS = auto()

    def label(self):
        if self == Filtering.NONE:
            return "None"
        if self == Filtering.LOWPASS:
            return "Low-pass"
        if self == Filtering.HIGHPASS:
            return "High-pass"
        if self == Filtering.BANDPASS:
            return "Band-pass"
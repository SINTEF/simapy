# Generated with Amplitude
# 
from enum import Enum
from enum import auto

class Amplitude(Enum):
    """"""
    DOWNCROSSING = auto()
    UPANDDOWNCROSSING = auto()

    def label(self):
        if self == Amplitude.DOWNCROSSING:
            return "Down crossing "
        if self == Amplitude.UPANDDOWNCROSSING:
            return "Up and down crossing"
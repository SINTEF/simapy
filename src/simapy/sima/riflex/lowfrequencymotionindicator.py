# Generated with LowFrequencyMotionIndicator
# 
from enum import Enum
from enum import auto

class LowFrequencyMotionIndicator(Enum):
    """"""
    NONE = auto()
    FILE = auto()

    def label(self):
        if self == LowFrequencyMotionIndicator.NONE:
            return "No low-freq. motions"
        if self == LowFrequencyMotionIndicator.FILE:
            return "Low freq. motion from file"
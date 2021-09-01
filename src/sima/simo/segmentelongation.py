# Generated with SegmentElongation
# 
from enum import Enum
from enum import auto

class SegmentElongation(Enum):
    """"""
    LINEAR = auto()
    CHARACTERISTIC = auto()

    def label(self):
        if self == SegmentElongation.LINEAR:
            return "Linear"
        if self == SegmentElongation.CHARACTERISTIC:
            return "Characteristic"
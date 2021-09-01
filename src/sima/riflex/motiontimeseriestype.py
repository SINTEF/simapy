# Generated with MotionTimeSeriesType
# 
from enum import Enum
from enum import auto

class MotionTimeSeriesType(Enum):
    """"""
    POSI = auto()
    DYND = auto()

    def label(self):
        if self == MotionTimeSeriesType.POSI:
            return "Global positions"
        if self == MotionTimeSeriesType.DYND:
            return "Global dynamic displacements"
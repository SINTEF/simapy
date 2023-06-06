# Generated with WindTimeSeriesMethod
# 
from enum import Enum
from enum import auto

class WindTimeSeriesMethod(Enum):
    """"""
    SAME = auto()
    SEPARATE = auto()

    def label(self):
        if self == WindTimeSeriesMethod.SAME:
            return "Same"
        if self == WindTimeSeriesMethod.SEPARATE:
            return "Separate"
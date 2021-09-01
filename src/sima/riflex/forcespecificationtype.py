# Generated with ForceSpecificationType
# 
from enum import Enum
from enum import auto

class ForceSpecificationType(Enum):
    """"""
    SIMPLE_EXPRESSION = auto()
    TIMESERIES_FROM_FILE = auto()

    def label(self):
        if self == ForceSpecificationType.SIMPLE_EXPRESSION:
            return "Forces described by simple expression"
        if self == ForceSpecificationType.TIMESERIES_FROM_FILE:
            return "Forces described by timeseries from file"
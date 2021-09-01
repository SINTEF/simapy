# Generated with StatisticsOperation
# 
from enum import Enum
from enum import auto

class StatisticsOperation(Enum):
    """"""
    MAX = auto()
    MAX_ABSOLUTE = auto()
    MIN = auto()
    MEAN = auto()
    STANDARD_DEVIATION = auto()

    def label(self):
        if self == StatisticsOperation.MAX:
            return "Maximum"
        if self == StatisticsOperation.MAX_ABSOLUTE:
            return "Maximum of absolute input values"
        if self == StatisticsOperation.MIN:
            return "Minimum"
        if self == StatisticsOperation.MEAN:
            return "Mean"
        if self == StatisticsOperation.STANDARD_DEVIATION:
            return "Standard deviation"
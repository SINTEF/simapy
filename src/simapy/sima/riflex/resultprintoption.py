# Generated with ResultPrintOption
# 
from enum import Enum
from enum import auto

class ResultPrintOption(Enum):
    """"""
    MOST_CRITICAL_POINT = auto()
    ALL_POINTS = auto()

    def label(self):
        if self == ResultPrintOption.MOST_CRITICAL_POINT:
            return "Most critical point"
        if self == ResultPrintOption.ALL_POINTS:
            return "All points"
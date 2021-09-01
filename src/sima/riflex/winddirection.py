# Generated with WindDirection
# 
from enum import Enum
from enum import auto

class WindDirection(Enum):
    """"""
    POSITIVE = auto()
    NEGATIVE = auto()

    def label(self):
        if self == WindDirection.POSITIVE:
            return "Positive"
        if self == WindDirection.NEGATIVE:
            return "Negative"
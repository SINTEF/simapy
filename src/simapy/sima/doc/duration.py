# Generated with Duration
# 
from enum import Enum
from enum import auto

class Duration(Enum):
    """"""
    MEDIUM = auto()
    FAST = auto()
    SLOW = auto()
    VERY_SLOW = auto()

    def label(self):
        if self == Duration.MEDIUM:
            return "Medium"
        if self == Duration.FAST:
            return "Fast"
        if self == Duration.SLOW:
            return "Slow"
        if self == Duration.VERY_SLOW:
            return "Very slow"
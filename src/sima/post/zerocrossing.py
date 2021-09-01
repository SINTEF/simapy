# Generated with ZeroCrossing
# 
from enum import Enum
from enum import auto

class ZeroCrossing(Enum):
    """"""
    UP = auto()
    DOWN = auto()
    ALL = auto()

    def label(self):
        if self == ZeroCrossing.UP:
            return "Up crossing"
        if self == ZeroCrossing.DOWN:
            return "Down crossing"
        if self == ZeroCrossing.ALL:
            return "All zero crossings"
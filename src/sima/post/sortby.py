# Generated with SortBy
# 
from enum import Enum
from enum import auto

class SortBy(Enum):
    """"""
    X_AXIS = auto()
    Y_AXIS = auto()

    def label(self):
        if self == SortBy.X_AXIS:
            return "X Axis"
        if self == SortBy.Y_AXIS:
            return "Y Axis"
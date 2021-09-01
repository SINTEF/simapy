# Generated with Iteration
# 
from enum import Enum
from enum import auto

class Iteration(Enum):
    """"""
    COLUMN = auto()
    GRID = auto()

    def label(self):
        if self == Iteration.COLUMN:
            return "Column"
        if self == Iteration.GRID:
            return "Grid"
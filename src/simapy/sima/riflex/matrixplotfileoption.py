# Generated with MatrixPlotFileOption
# 
from enum import Enum
from enum import auto

class MatrixPlotFileOption(Enum):
    """"""
    NO_PRINT = auto()
    MIN_AND_STANDARD_DEV = auto()
    MIN_MAX_AND_STANDARD_DEV = auto()
    MAX_STATISTICS = auto()

    def label(self):
        if self == MatrixPlotFileOption.NO_PRINT:
            return "No print"
        if self == MatrixPlotFileOption.MIN_AND_STANDARD_DEV:
            return "Min, max and standard deviation"
        if self == MatrixPlotFileOption.MIN_MAX_AND_STANDARD_DEV:
            return "Min, max, mean, standard deviation, mean period"
        if self == MatrixPlotFileOption.MAX_STATISTICS:
            return "Max amount of statistics"
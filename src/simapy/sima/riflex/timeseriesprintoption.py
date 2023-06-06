# Generated with TimeSeriesPrintOption
# 
from enum import Enum
from enum import auto

class TimeSeriesPrintOption(Enum):
    """"""
    NO_PRINT = auto()
    PRINT_Y_Z = auto()
    PRINT_Y_Z_SKIP_FATIGUE = auto()

    def label(self):
        if self == TimeSeriesPrintOption.NO_PRINT:
            return "No print"
        if self == TimeSeriesPrintOption.PRINT_Y_Z:
            return "Print Y and Z curvature"
        if self == TimeSeriesPrintOption.PRINT_Y_Z_SKIP_FATIGUE:
            return "Print Y and Z curvature - skip fatigue calculation"
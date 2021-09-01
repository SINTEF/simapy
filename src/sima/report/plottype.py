# Generated with PlotType
# 
from enum import Enum
from enum import auto

class PlotType(Enum):
    """"""
    LINE = auto()
    SCATTER = auto()
    BAR = auto()

    def label(self):
        if self == PlotType.LINE:
            return "Line"
        if self == PlotType.SCATTER:
            return "Scatter"
        if self == PlotType.BAR:
            return "Bar"
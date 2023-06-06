# Generated with PlotSize
# 
from enum import Enum
from enum import auto

class PlotSize(Enum):
    """"""
    DYNAMIC = auto()
    FIXED = auto()
    FIXED_ASPECT_RATIO = auto()

    def label(self):
        if self == PlotSize.DYNAMIC:
            return "Dynamic"
        if self == PlotSize.FIXED:
            return "Fixed size"
        if self == PlotSize.FIXED_ASPECT_RATIO:
            return "Fixed Aspect Ratio"
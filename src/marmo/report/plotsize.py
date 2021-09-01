# Generated with PlotSize
# 
from enum import Enum
from enum import auto

class PlotSize(Enum):
    """"""
    dynamic = auto()
    fixed = auto()
    fixed_aspect_ratio = auto()

    def label(self):
        if self == PlotSize.dynamic:
            return "Dynamic"
        if self == PlotSize.fixed:
            return "Fixed"
        if self == PlotSize.fixed_aspect_ratio:
            return "Fixed Aspect Ratio"
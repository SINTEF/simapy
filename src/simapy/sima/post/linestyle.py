# Generated with LineStyle
# 
from enum import Enum
from enum import auto

class LineStyle(Enum):
    """"""
    SOLID = auto()
    DASH = auto()
    BAR = auto()
    POINT = auto()

    def label(self):
        if self == LineStyle.SOLID:
            return "Solid line"
        if self == LineStyle.DASH:
            return "Dash Line"
        if self == LineStyle.BAR:
            return "Bar"
        if self == LineStyle.POINT:
            return "Point"
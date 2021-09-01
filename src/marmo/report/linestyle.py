# Generated with LineStyle
# 
from enum import Enum
from enum import auto

class LineStyle(Enum):
    """"""
    solid = auto()
    dash = auto()
    bar = auto()
    point = auto()

    def label(self):
        if self == LineStyle.solid:
            return "Solid line"
        if self == LineStyle.dash:
            return "Dashed line"
        if self == LineStyle.bar:
            return "Bar plot"
        if self == LineStyle.point:
            return "Points only"
# Generated with PointStyle
# 
from enum import Enum
from enum import auto

class PointStyle(Enum):
    """"""
    none = auto()
    point = auto()
    circle = auto()
    square = auto()

    def label(self):
        if self == PointStyle.none:
            return "None"
        if self == PointStyle.point:
            return "Point"
        if self == PointStyle.circle:
            return "Circle"
        if self == PointStyle.square:
            return "Square"
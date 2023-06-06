# Generated with PointStyle
# 
from enum import Enum
from enum import auto

class PointStyle(Enum):
    """"""
    NONE = auto()
    POINT = auto()
    CIRCLE = auto()
    SQUARE = auto()

    def label(self):
        if self == PointStyle.NONE:
            return "None"
        if self == PointStyle.POINT:
            return "Point"
        if self == PointStyle.CIRCLE:
            return "Circle"
        if self == PointStyle.SQUARE:
            return "Square"
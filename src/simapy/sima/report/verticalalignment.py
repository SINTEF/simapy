# Generated with VerticalAlignment
# 
from enum import Enum
from enum import auto

class VerticalAlignment(Enum):
    """"""
    TOP = auto()
    CENTER = auto()
    BOTTOM = auto()

    def label(self):
        if self == VerticalAlignment.TOP:
            return "Top"
        if self == VerticalAlignment.CENTER:
            return "Center"
        if self == VerticalAlignment.BOTTOM:
            return "Bottom"
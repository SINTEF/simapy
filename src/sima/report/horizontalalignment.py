# Generated with HorizontalAlignment
# 
from enum import Enum
from enum import auto

class HorizontalAlignment(Enum):
    """"""
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()

    def label(self):
        if self == HorizontalAlignment.LEFT:
            return "Left"
        if self == HorizontalAlignment.CENTER:
            return "Center"
        if self == HorizontalAlignment.RIGHT:
            return "Right"
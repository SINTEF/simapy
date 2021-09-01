# Generated with Orientation
# 
from enum import Enum
from enum import auto

class Orientation(Enum):
    """"""
    PORTRAIT = auto()
    LANDSCAPE = auto()

    def label(self):
        if self == Orientation.PORTRAIT:
            return "Portrait"
        if self == Orientation.LANDSCAPE:
            return "Landscape"
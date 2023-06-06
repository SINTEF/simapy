# Generated with Volume
# 
from enum import Enum
from enum import auto

class Volume(Enum):
    """"""
    ADD = auto()
    SUBTRACT = auto()

    def label(self):
        if self == Volume.ADD:
            return "Add"
        if self == Volume.SUBTRACT:
            return "Subtract"
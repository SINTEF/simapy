# Generated with QtfInput
# 
from enum import Enum
from enum import auto

class QtfInput(Enum):
    """"""
    MANUAL = auto()
    FILE = auto()

    def label(self):
        if self == QtfInput.MANUAL:
            return "Manual"
        if self == QtfInput.FILE:
            return "File"
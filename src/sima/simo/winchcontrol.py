# Generated with WinchControl
# 
from enum import Enum
from enum import auto

class WinchControl(Enum):
    """"""
    PREDEFINED = auto()
    HLA = auto()
    EXTERNAL = auto()

    def label(self):
        if self == WinchControl.PREDEFINED:
            return "Predefined"
        if self == WinchControl.HLA:
            return "HLA"
        if self == WinchControl.EXTERNAL:
            return "External"
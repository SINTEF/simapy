# Generated with PeakType
# 
from enum import Enum
from enum import auto

class PeakType(Enum):
    """"""
    LOCAL = auto()
    GLOBAL = auto()
    BLOCK = auto()

    def label(self):
        if self == PeakType.LOCAL:
            return "Local"
        if self == PeakType.GLOBAL:
            return "Global"
        if self == PeakType.BLOCK:
            return "Block"